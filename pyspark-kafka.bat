@REM spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 --repositories https://repo1.maven.org/maven2/ pyspark-kafka.py

@REM spark-submit --jars C:\Sotiris\kafka\jars\spark-sql-kafka-0-10_2.12-3.3.0.jar,C:\Sotiris\kafka\jars\kafka-clients-3.3.0.jar,C:\Sotiris\kafka\jars\spark-streaming-kafka-0-10-assembly_2.12-3.3.0.jar,C:\Sotiris\kafka\jars\spark-streaming-kafka-0-10_2.12-3.3.0.jar,C:\Sotiris\kafka\jars\commons-pool2-2.12.0.jar  pyspark-kafka.py

@REM spark-submit --conf "spark.executor.extraJavaOptions=-Dcom.sun.net.ssl.checkRevocation=false" --conf "spark.driver.extraJavaOptions=-Dcom.sun.net.ssl.checkRevocation=false" --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0  pyspark-kafka.py
spark-submit pyspark-kafka.py