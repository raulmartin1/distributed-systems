import Pyro4

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")  # Permite que todos los clientes compartan el mismo objeto
class Observable:
    
    def __init__(self):
        self.observers = [] # Llista per guardar observers

    def register_ob(self, observer_uri):
        """Metodo para registrar observers"""
        observer = Pyro4.Proxy(observer_uri)
        self.observers.append(observer)
        print(f"Observer {observer_uri} registrado")

    def unregister_ob(self, observer_uri):
        """Metodo para eliminar observers"""
        self.observers = [obs for obs in self.observers if obs._pyroUri != observer_uri]
        print(f"Observer {observer_uri} eliminado")

    def notify_obs(self, message):
        for observer in self.observers:
            observer.update(message)


def main():
    daemon = Pyro4.Daemon()     # Crear un servidor Pyro Daemon
    ns = Pyro4.locateNS()       # Localizar el Name Server
    observable = Observable()   # Instanciar el objeto observable
    uri = daemon.register(observable)  # Registrar el objeto
    ns.register("example.observable", uri)  # Registrar en el Name Server

    print(f"Servidor Observable corriendo en URI: {uri}")
    daemon.requestLoop()  # Mantener el servidor en espera

if __name__ == "__main__":
    main()
