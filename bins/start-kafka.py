import subprocess
import time
import os

bin_path = r"C:\Sotiris\kafka\3.5.1"

def start_zookeeper():
    subprocess.Popen([ os.path.join(bin_path,"bin", "windows", "zookeeper-server-start.bat") , os.path.join(bin_path,"config","zookeeper.properties") ])

def start_kafka():
    subprocess.Popen([ os.path.join(bin_path,"bin", "windows", "kafka-server-start.bat") , os.path.join(bin_path,"config","server.properties") ])

if __name__ == "__main__":
    # Start Zookeeper
    start_zookeeper()

    # Wait for Zookeeper to start (you might need to adjust the sleep time)
    time.sleep(15)

    # Start Kafka
    start_kafka()

    # Wait for Kafka to start (you might need to adjust the sleep time)
    time.sleep(15)
