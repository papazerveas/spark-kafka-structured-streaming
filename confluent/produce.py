from confluent_kafka import Producer
from protobuf import addressbook_pb2

# p.produce('mytopic', 'my message')
# p.flush()

person = addressbook_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.PHONE_TYPE_HOME

serialized_data = person.SerializeToString()

p = Producer({'bootstrap.servers': 'localhost:9092', 'acks': 'all'})
p.produce('sql-insert', serialized_data)
p.flush()