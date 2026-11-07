from spyne import Application, rpc, ServiceBase, Integer
from spyne.error import ArgumentError
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

from wsgiref.simple_server import make_server


class CalculadoraService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def sumar(ctx, a, b):
        return a + b

    @rpc(Integer, Integer, _returns=Integer)
    def restar(ctx, a, b):
        return a - b

    @rpc(Integer, Integer, _returns=Integer)
    def multiplicar(ctx, a, b):
        return a * b

    @rpc(Integer, Integer, _returns=Integer)
    def dividir(ctx, a, b):
        if b == 0:
            raise ArgumentError("No se permite la división entre cero.")
        return a // b


application = Application(
    [CalculadoraService],
    tns='calculadora.soap',
    name='CalculadoraService',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

wsgi_app = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('0.0.0.0', 8000, wsgi_app)
    print("Servidor corriendo en http://127.0.0.1:8000")
    print("WSDL disponible en: http://127.0.0.1:8000/?wsdl")
    server.serve_forever()