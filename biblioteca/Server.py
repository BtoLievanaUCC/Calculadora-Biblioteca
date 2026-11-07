from wsgiref.simple_server import make_server

from spyne import Application, ServiceBase, rpc
from spyne.model.primitive import Boolean, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

# Catálogo en memoria: codigo -> (titulo, ejemplares)
CATALOGO = {
    "LIB-001": ("Cien años de soledad", 3),
    "LIB-002": ("La vorágine", 0),
}


class BibliotecaService(ServiceBase):

    @rpc(Unicode, _returns=Unicode)
    def buscar_titulo(ctx, codigo):
        titulo, _ = CATALOGO.get(codigo, ("No encontrado", 0))
        return titulo

    @rpc(Unicode, _returns=Integer)
    def ejemplares_disponibles(ctx, codigo):
        _, ejemplares = CATALOGO.get(codigo, ("No encontrado", 0))
        return ejemplares

    @rpc(Unicode, _returns=Boolean)
    def hay_disponibilidad(ctx, codigo):
        _, ejemplares = CATALOGO.get(codigo, ("No encontrado", 0))
        return ejemplares > 0


application = Application(
    [BibliotecaService],
    tns="http://biblioteca.universidad.edu/soap",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(),
)

if __name__ == "__main__":
    wsgi_app = WsgiApplication(application)
    servidor = make_server("127.0.0.1", 8000, wsgi_app)
    print("Servicio SOAP en http://127.0.0.1:8000/?wsdl")
    servidor.serve_forever()