#!# -*- coding; utf-8 -*-
import pika
import subprocess
import Image
import base64

credentials = pika.PlainCredentials('rodrigo', 'rodrigo') 

parameters = pika.ConnectionParameters('192.168.1.196', 5672, '/rodrigo', credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

def fib(n):
    return n

def on_request(ch, method, props, body):
    string = str(body)

    print(body)
    
    imgdata = base64.b64decode(body)
    filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)
    
    response = fib(body)
    channel.stop_consuming()

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response)),
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()
