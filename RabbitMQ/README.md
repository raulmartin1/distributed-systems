# 🚀 RabbitMQ InsultService

Aquest repositori conté un servei basat en **RabbitMQ** per gestionar una cua de missatges i un sistema de publicació/subscripció.

## 📌 Serveis Implementats

### 🔄 Cua amb RabbitMQ
- **📝 InsultProducer**: Genera nous insults cada **5 segons** i els envia a la cua de RabbitMQ.
- **📥 InsultConsumer**: Llegeix insults de la cua de RabbitMQ i els desa en una llista Redis (`INSULTS`) només si són nous.

### 📡 Sistema Pub/Sub amb RabbitMQ
- **📢 InsultBroadcaster**: Publica insults de la llista `INSULTS` a un canal de subscripció de RabbitMQ.
- **👂 InsultReceiver**: Subscriu-se al canal del broadcaster per rebre insults en temps real.
  - Pots executar diversos **InsultReceiver** per comprovar el funcionament.

## 🛠️ Instal·lació i Execució

### 🔹 1. Executar RabbitMQ amb Docker
```bash
docker pull rabbitmq:management
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management