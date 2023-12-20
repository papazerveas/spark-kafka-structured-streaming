import subprocess
import time
import os

bin_path = r"C:\Sotiris\kafka\3.5.1"

def stop_zookeeper():
    subprocess.Popen([ os.path.join(bin_path,"bin", "windows", "zookeeper-server-stop.bat")   ])

def stop_kafka():
    subprocess.Popen([ os.path.join(bin_path,"bin", "windows", "kafka-server-stop.bat")  ])

if __name__ == "__main__":
    # Stop Kafka
    stop_kafka()

    # Stop Zookeeper
    stop_zookeeper()
