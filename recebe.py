#!# -*- coding; utf-8 -*-
import pika
import subprocess
import Image
import base64
import time

credentials = pika.PlainCredentials('rodrigo', 'rodrigo') 

parameters = pika.ConnectionParameters('192.168.11.74 ', 5672, '/rodrigo', credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='rpc_queue')
a = "a"

def fib():
    arq = open("str.txt", "w")
    str = None
    with open("img/0.png", "rb") as imageFile:
        str = base64.b64encode(imageFile.read())
    arq.write(str)
    arq.close()

    arq = open("str.txt", "r")
    string = arq.read()
    print(string)
    arq.close()
    return string
    
def on_request(ch, method, props, body):
    string = body
    ant = None
    
    if len(body) > 1000:
        imgdata = base64.b64decode(body)
        filename = 'img/temer.jpg'  # I assume you have a way of picking unique filenames

        with open(filename, 'wb') as f:
            f.write(imgdata)

        filename = 'img/0.png'  # I assume you have a way of picking unique filenames

        with open(filename, 'wb') as f:
            f.write(imgdata)
        ant = body

    py_arq = "niveis_de_cinza2.py"
    arq = open(py_arq, "w")
    arq.write(string)
    arq.close()

    start = time.time()
    processo = subprocess.call(["python "+py_arq], shell=True)
    
    response = fib()
    print(response)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()
