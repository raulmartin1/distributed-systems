import Pyro4

missatge = "HOLA"

echo_maker = Pyro4.Proxy("PYRONAME:echo.server")
print(echo_maker.echo(missatge))