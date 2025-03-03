import Pyro4


@Pyro4.expose
class EchoServer:
    def echo(self, message):
        return f"{message}"

daemon = Pyro4.Daemon()             # Crear un server Pyro Daemon
ns = Pyro4.locateNS()               # Buscar el Name Server
uri = daemon.register(EchoServer)   # Registrar el objeto
ns.register("echo.server", uri)     # Registrar el objeto usand el echo.server

print("Ready.")
daemon.requestLoop()                # Empieza el bucle del servidor para peticiones

