#!/usr/bin/env python
import pika
import uuid
import os
from threading import Thread
import Image
import base64
 
class FibonacciRpcClient(Thread):

    def __init__(self,num):
        Thread.__init__(self)

        result = channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def run(self):
        print(" [x] Enviando")
        str = None
        with open("temer.jpg", "rb") as imageFile:
            str = base64.b64encode(imageFile.read())
        response = a.call(str)

        arq = open("niveis_de_cinza.py", "r")
        chamada = arq.read()
        print(chamada)
        arq.close()
        response = a.call(chamada)

        print(" %r" % response)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(n))
        while self.response is None:
            connection.process_data_events()
        return self.response

credentials = pika.PlainCredentials('rodrigo', 'rodrigo') 

parameters = pika.ConnectionParameters('localhost', 5672, '/rodrigo', credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

num = "1"
a = FibonacciRpcClient(num)
a.start()

