# 🚀 Redis InsultService

Aquest repositori conté un servei basat en **Redis** per gestionar una cua de missatges i un sistema de publicació/subscripció.

## 📌 Serveis Implementats  

### 🔄 Cua amb Redis Blocking Queue  
- **📝 InsultProducer**: Genera nous insults cada **5 segons** i els envia a la cua.  
- **📥 InsultConsumer**: Llegeix insults de la cua i els desa en una llista Redis (`INSULTS`) només si són nous.  

### 📡 Sistema Pub/Sub amb Redis  
- **📢 InsultBroadcaster**: Publica insults de la llista `INSULTS` a un canal de subscripció.  
- **👂 InsultReceiver**: Subscriu-se al canal del broadcaster per rebre insults en temps real.  
  - Pots executar diversos **InsultReceiver** per comprovar el funcionament.  

## 🛠️ Instal·lació i Execució  

### 🔹 1. Executar Redis amb Docker  
```bash
docker pull redis
docker run --name my-redis -d -p 6379:6379 redis
docker exec -it my-redis redis-cli
