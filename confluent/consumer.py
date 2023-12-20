from confluent_kafka import Consumer
from protobuf import addressbook_pb2

c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'mygroup'})
c.subscribe(['sql-insert'])
while True:
    msg = c.poll(1.0)
    if msg is None:
        # print("next")
        continue
    if msg.error():
        print('Error: {}'.format(msg.error()))
        continue

    new_person = addressbook_pb2.Person()
    serialized_data = msg.value()
    new_person.ParseFromString(serialized_data)
    print(new_person)
    #print('Received message: {}'.format(msg.value().decode('utf-8')))
