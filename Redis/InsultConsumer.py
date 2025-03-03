import redis
# Connect to Redis
client = redis.Redis(host='localhost', port=6379, db=0,
decode_responses=True)
queue_name = "insult_queue"
list="INSULTS"

print("InsultConsumer: esperando para recibir insultos...")
while True:
    task = client.blpop(queue_name, timeout=0) # Espera un insulto
    if task:
        insult = task[1]
        if not client.sismember(list, insult): # Comrpovar que no esta a la lista
            client.rpush(list, insult)
            print(f"InsultConsumer: Insulto '{insult}' agregado ")
        else:
            print(f"InsultConsumer: Insulto '{insult}' ya esta en al lista ")