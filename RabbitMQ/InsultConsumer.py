import pika
import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)


# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue (ensure it exists)
queue_name = "insult_queue"
channel.queue_declare(queue=queue_name)

print("InsultConsumer: Esperando insultos...")

# Define the callback function
def callback(ch, method, properties, body):
    insult = body.decode() # Los mensajes en RAbbitQ llegan en bytes, pasarlo a string
    print(f"InusltConsumer: Insulto '{insult}' recibido")

    # Obtener todos los insultos almacenados en la lista 'INSULTS'
    existing_insults = redis_client.lrange("INSULTS", 0, -1)
    if insult not in existing_insults:
        redis_client.rpush("INSULTS", insult)
        print(f"InsultConsumer: Insulto '{insult}' añadido a  la lista INSULTS")

# Consume messages
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('InsultConsumer: Esperando mensajes. Para salir, pulsa CTRL+C')
channel.start_consuming()
