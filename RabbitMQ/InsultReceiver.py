import pika

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare exchange
exchange_name = 'insult_exchange'
channel.exchange_declare(exchange=exchange_name, exchange_type='fanout')

# Create a new temporary queue (random name, auto-delete when consumer disconnects)
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# Bind the queue to the exchange
channel.queue_bind(exchange=exchange_name, queue=queue_name)

print("InsultReceiver: esperando insultos. Para salir, presiona CTRL+C")

# Define callback function
def callback(ch, method, properties, body):
    insult = body.decode()
    print(f"InsultReceiver: Insulto '{insult} recibido'")

# Consume messages
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
