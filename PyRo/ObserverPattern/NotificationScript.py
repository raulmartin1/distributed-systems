import Pyro4

def main():
    observable = Pyro4.Proxy("PYRONAME:example.observable")
    observable.notify_obs("Hello, Observers!")

if __name__ == "__main__":
    main()

