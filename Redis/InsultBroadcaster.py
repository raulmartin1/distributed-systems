import redis
import time
# Connect to Redis
client = redis.Redis(host='localhost', port=6379, db=0,
decode_responses=True)
channel_name = "insult_channel"
list="INSULTS"

print("InsultConsumer: enviando insultos desde la lista INSULTS")
while True:
    
    insult = client.lpop(list) # Cogemos primer insulto
    if insult:
        client.publish(channel_name, insult)            
        print(f"InsultBroadcaster: Insulto '{insult}' publicado ")
    else:
        print(f"InsultBroadcaster: No hay insulto para publicar")
    
    time.sleep(2) # Simulating delay between messages