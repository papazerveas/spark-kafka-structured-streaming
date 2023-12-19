import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.3.0,org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 pyspark-shell'

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

# Create a Spark session
#   config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0,org.apache.kafka:kafka-clients:3.3.0"). \
jars = os.getcwd() + "/jars/spark-sql-kafka-0-10_2.12-3.3.0.jar" + "," + os.getcwd() + "/jars/kafka-clients-3.3.0.jar"
# config("spark.jars", jars).\
    
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
  
  
# Convert the value column to a string (assuming the value contains the actual data)
stream_df = raw_stream_df.selectExpr("CAST(value AS STRING)")

# Define your processing logic
# For example, you can split the data by a delimiter
words = stream_df.select(explode(split("value", " ")).alias("word"))


wordCounts = words.groupBy("word").count()


# Define the output sink (e.g., console, Kafka, or other supported sinks)
query = wordCounts \
        .writeStream \
        .trigger(processingTime='2 seconds') \
        .outputMode("complete") \
        .format("console").start()

# Start the streaming query
query.awaitTermination()
