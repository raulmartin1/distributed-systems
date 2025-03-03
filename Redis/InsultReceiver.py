import redis
# Connect to Redis
client = redis.Redis(host='localhost', port=6379, db=0,
decode_responses=True)
channel_name = "insult_channel"

# Subscribe to channel
pubsub = client.pubsub()
pubsub.subscribe(channel_name)

print(f"InsultReceiver: Suscrito al canal '{channel_name}' esperando insultos...")
# Continuously listen for messages
for message in pubsub.listen():
    if message["type"] == "message":
        print(f"InsultReceiver: Insulto '{message['data']}' recibido ")