'''

Created on 2018年1月8日

@author: Administrator
'''

# e11170b8cbd2d74102651cb967fa28e5
# e11170b8cbd2d74102651cb967fa28e5
# 
# e8248cbe79a288ffec75d7300ad2e07172f487f6
# e8248cbe79a288ffec75d7300ad2e07172f487f6


from pykafka import KafkaClient
import logging
import threading
import time
import rapidjson as json

logging.basicConfig(level = logging.INFO)

class Producer(threading.Thread):

    def __init__(self, host, name, topicname):
        super(Producer, self).__init__(name=name)
        self.__host = host
        self.__topicname = topicname

    def __connect(self):
        self.__client = KafkaClient(hosts = self.__host)
        print(self.__client.topics)
        self.__topic = self.__client.topics[self.__topicname]
        return True

    def run(self):
        threading.Thread.run(self)

        if not self.__connect():
            return

        while True:
            with self.__topic.get_sync_producer() as producer:
                data = {'a':'bbbb', 'b':10.20, 'c':True, 'd':[0,1,2,3,4,5,6,7,8,9]}
                s = json.dump(data)
                producer.produce(bytes(s, encoding='utf-8'))

            time.sleep(2)

class Consumer(threading.Thread):
    def __init__(self, host, name, topicname):
        super(Consumer, self).__init__(name=name)
        self.__host = host
        self.__topicname = topicname

    def __connect(self):
        self.__client = KafkaClient(hosts = self.__host)
        print(self.__client.topics)
        self.__topic = self.__client.topics[self.__topicname]
        return True

    def run(self):
        threading.Thread.run(self)

        if not self.__connect():
            return
        
        while True:
            consumer = self.__topic.get_simple_consumer(consumer_timeout_ms = 5)
            for message in consumer:
                if message is not None:
                    print(message.offset, message.value)

#生产kafka数据，通过字符串形式
def kafka_produce_data(topic):
    with topic.get_sync_producer() as producer:
        for i in range(4):
            producer.produce(bytes('message', encoding='utf-8'))

#消费kafka数据
def kafka_consume_data(topic, timeout):
    consumer = topic.get_simple_consumer(consumer_timeout_ms = timeout)
    for message in consumer:
        if message is not None:
            print(message.offset, message.value)

if __name__ == '__main__':
#     client = KafkaClient(hosts = "192.168.20.2:9092")
#     client = KafkaClient(hosts = "192.168.20.4:9092")
#     client = KafkaClient(hosts = "192.168.20.6:9092")
#     print(client.topics)
#     topic = client.topics[b'znap_pm_kpi_monitor_change']
#     kafka_produce_data(topic)
# 
#     print(client.topics)
# 
#     kafka_consume_data(topic, 1)

#     procducer = Producer("192.168.20.6:9092", 'Producer', b'znap_pm_kpi_monitor_change')
#     procducer.start()

    consumer = Consumer("192.168.20.6:9092", 'Consumer', b'znap_pm_kpi_monitor_change')
    consumer.start()

    input()
