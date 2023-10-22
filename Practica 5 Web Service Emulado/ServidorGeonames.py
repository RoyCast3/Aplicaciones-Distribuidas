import http.server
import socketserver
import json

# Datos ficticios de temperatura para países de América Latina
estadosMX = {
    "Mexico",
    "CDMX",
    "Hidalgo",
    "Guerrero",
    "Monterrey",
}
estadosUSA = {
    "Florida",
    "Texas",
    "California",
    "Oregon",
    "Alaska",
}
estadosCanada = {
    "Alberta",
    "Ontario",
    "Quebec",
    "Yukon",
}

# Clase personalizada para manejar las solicitudes
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/location/'):
            estado = self.path[10:]
            print(f'Ubicacion: {estado}')
            if estado in estadosMX:
                data = {"location": "Mexico"}
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())  # Codificar la cadena a bytes
            elif estado in estadosUSA:
                data = {"location": "USA"}
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())
            elif estado in estadosCanada:
                data = {"location": "Canada"}
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())    
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write("Pais no encontrado.".encode())  # Codificar la cadena a bytes
        else:
            super().do_GET()

# Configuración del servidor
with socketserver.TCPServer(("", 9090), MyHandler) as httpd:
    print("Servidor web en el puerto 9090")
    httpd.serve_forever()
