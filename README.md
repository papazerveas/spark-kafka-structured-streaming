# spark

## setup
```
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
start-zookeper.bat
start-kafka.bat
kafka-create-producer.bat
kafka-create-consumer.bat
pyspark-kafka.bat
```
