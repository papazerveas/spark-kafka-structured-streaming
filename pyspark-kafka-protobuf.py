from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from confluent.protobuf import addressbook_pb2

spark = SparkSession.builder.master("local").\
    appName("kafka-example").getOrCreate()


raw_stream_df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "sql-insert") \
    .option("maxOffsetsPerTrigger", "100") \
    .option("startingOffsets", "earliest")\
    .load()


def protobuf_deserializer(message):
    """udf function to deserialize protobuf

    Args:
        message (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        if isinstance(message, bytearray):
            message = bytes(message)
        person = addressbook_pb2.Person()
        person.ParseFromString(bytes(message))
        return person.name, person.id, person.email
    except Exception as e:
        return str(message), -1, str(e)

schema = StructType([
    StructField("name", StringType(), True),
    StructField("id", IntegerType(), True),
    StructField("email", StringType(), True)
])

proto_udf = udf(protobuf_deserializer, schema)

deserialized_df = raw_stream_df.withColumn("deserialized", proto_udf("value"))

stream_df = deserialized_df \
    .withColumn("name", col("deserialized.name"))  \
    .withColumn("id", col("deserialized.id")) \
    .withColumn("email",  col("deserialized.email")) \
    .drop(col("deserialized")) \
    .filter(col("id") != -1)

# Define the output sink (e.g., console, Kafka, or other supported sinks)
query = stream_df \
    .writeStream \
    .trigger(processingTime='2 seconds') \
    .outputMode("append") \
    .option("truncate", "true") \
    .format("console").start()

# Start the streaming query
query.awaitTermination()
