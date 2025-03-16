import time
import pika

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue
queue_name = "insult_queue"
channel.queue_declare(queue=queue_name)

insults = ["Tonto", "Bobo", "Pavo"]
print("InsultProducer: Enviando insultos cada 5 segundos")

for insult in insults:
    # Publish a message
    channel.basic_publish(exchange='', routing_key=queue_name, body=insult)
    print(f"InsultProducer: Insulto '{insult}' enviado")
    time.sleep(5)

# Close connection
connection.close()
