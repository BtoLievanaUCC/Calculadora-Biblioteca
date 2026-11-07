from zeep import Client
 
client = Client("http://127.0.0.1:8000/?wsdl")
 
CODIGOS = ["LIB-001", "LIB-002", "LIB-999"]
 
print(f"{'Código':<10}{'buscar_titulo':<25}{'Ejempl.':<10}{'Disp.'}")
for codigo in CODIGOS:
    titulo = client.service.buscar_titulo(codigo)
    ejemplares = client.service.ejemplares_disponibles(codigo)
    disponible = client.service.hay_disponibilidad(codigo)
    print(f"{codigo:<10}{titulo:<25}{ejemplares:<10}{disponible}")
 
