import pika
import redis

# Conectar a Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a fanout exchange
exchange_name = 'insult_exchange'
channel.exchange_declare(exchange=exchange_name, exchange_type='fanout')

insults = redis_client.lrange("INSULTS", 0, -1)
if not insults:
        print("InsultBroadcaster: No hay insultos en la lista INSULTS")
else:
        for insult in insults:
                # Publish a message
                channel.basic_publish(exchange=exchange_name, routing_key='', body=insult)
                print(f"InsultBroadcaster: Insulto '{insult}' publicado")

# Close connection
connection.close()
