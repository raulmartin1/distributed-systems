# 🔥 Pyro4: Exercicis de Comunicació Remota

Aquest repositori conté exercicis per entendre **Pyro4**, una biblioteca per a **RPC (Remote Procedure Call) en Python**.

## 📌 Exercicis

### 🚀 Exercici 1: EchoServer  
- **🖥️ Servidor:** Defineix `EchoServer`, el registra en el **Name Server** com `"echo.server"` i espera peticions.  
- **💻 Client:** Recupera l’objecte remot i crida `echo("HOLA")`.

### 📡 Exercici 2: Patró Observer  
- **🖥️ Servidor Observable:** Registra `"example.observable"`, permet registrar observadors i enviar notificacions.  
- **👀 Client Observer:** Es registra per rebre missatges.  
- **🔔 Script de Notificació:** Envia missatges als observadors.

## 🚀 Execució  
1. **Iniciar el Name Server:**  
   ```bash
   python -m Pyro4.naming
