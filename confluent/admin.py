from confluent_kafka.admin import AdminClient, NewTopic
admin_client = AdminClient({
    "bootstrap.servers": "localhost:9092"
})
admin_client.list_topics().topics

topic_list = []
topic_list.append(NewTopic("sql-insert", 1, 1))
admin_client.create_topics(topic_list)
