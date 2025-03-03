import Pyro4

@Pyro4.expose
class Observable:
     def update(self, message):
        """Este metodo es llamado cuando la clase Observable envia una notificacion"""
        print(f"Notificacion actualizada: {message}")

def main():
    ns = Pyro4.locateNS()
    observable = Pyro4.Proxy(ns.lookup("example.observable"))

    with Pyro4.Daemon() as daemon:
        observer = Observable()
        observer_uri = daemon.register(observer)    # Obtener el URI

        observable.register_ob(observer_uri)        # Registrar un oberver

        print(f"Observer registrado con la URI: {observer_uri}")
        print("Esperando para la notificacion...")

        daemon.requestLoop()    # Mantener los observadores recibiendo notificaiones

if __name__ == "__main__":
    main()
