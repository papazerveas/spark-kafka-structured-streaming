# spark

## setup

```text
commons-pool2-2.12.0.jar
spark-streaming-kafka-0-10-assembly_2.12-3.3.0.jar
spark-streaming-kafka-0-10_2.12-3.3.0.jar
spark-sql-kafka-0-10_2.12-3.3.0.jar
kafka-clients-3.3.0.jar

copy jars to $SPARK_HOME/jars
```

### loging

```text
log4j2.properties => rootLogger.level = error
```

### spark-defaults.conf

```sh
spark.driver.extraClassPath       $SPARK_HOME/jars/*.jar
spark.executor.extraClassPath     $SPARK_HOME/jars/*.jar
```

## start

```bash
bins\start-all.bat

or 
bins\start-zookeper.bat
bins\start-kafka.bat

```

## produce - consume - text

```sh
bins\kafka-create-consumer.bat
bins\kafka-create-producer.bat
spark-submit pyspark-kafka-text.py
```

### protobuf

```sh
    scoop install protobuf
    protoc -I=confluent/protobuf --python_out=confluent/protobuf addressbook.proto

    -I = input path
  --python_out=OUT_DIR        Generate Python source file.
```

## produce - consume - protobuf

```sh
python .\confluent\consumer.py
python .\confluent\produce.py
spark-submit pyspark-kafka-protobuf.py or pyspark-kafka.bat
```

## spark output

```sh
-------------------------------------------
Batch: 0
-------------------------------------------
+----+--------------------+----------+---------+------+--------------------+-------------+--------+----+----------------+
| key|               value|     topic|partition|offset|           timestamp|timestampType|    name|  id|           email|
+----+--------------------+----------+---------+------+--------------------+-------------+--------+----+----------------+
|null|             [68 69]|sql-insert|        0|     1|2023-12-19 23:01:...|            0|        |   0|                |
|null|[73 74 61 72 74 2...|sql-insert|        0|     9|2023-12-19 23:15:...|            0|        |   0|                |
|null|[0A 08 4A 6F 68 6...|sql-insert|        0|    20|2023-12-20 09:54:...|            0|John Doe|1234|jdoe@example.com|
|null|[0A 08 4A 6F 68 6...|sql-insert|        0|    21|2023-12-20 09:58:...|            0|John Doe|1234|jdoe@example.com|
|null|[0A 08 4A 6F 68 6...|sql-insert|        0|    22|2023-12-20 12:34:...|            0|John Doe|1234|jdoe@example.com|
|null|[0A 08 4A 6F 68 6...|sql-insert|        0|    23|2023-12-20 12:58:...|            0|John Doe|1234|jdoe@example.com|
|null|[0A 08 4A 6F 68 6...|sql-insert|        0|    24|2023-12-20 12:59:...|            0|John Doe|1234|jdoe@example.com|
+----+--------------------+----------+---------+------+--------------------+-------------+--------+----+----------------+
```
