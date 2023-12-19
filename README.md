# spark

## copy jars to $SPARK_HOME/jars

### loging
log4j2.properties => rootLogger.level = error

### spark-defaults.conf
spark.driver.extraClassPath       $SPARK_HOME/jars/*.jar
spark.executor.extraClassPath     $SPARK_HOME/jars/*.jar


## start

start-zookeper.bat
start-kafka.bat
kafka-create-producer.bat
kafka-create-consumer.bat
pyspark-kafka.bat
