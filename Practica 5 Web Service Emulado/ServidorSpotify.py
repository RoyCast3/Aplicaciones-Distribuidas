import http.server
import socketserver
import json
import random

# Datos ficticios de temperatura para países de América Latina
usuarios = {
    "Mexico": "\nMusica Clasica \nRock 80's",
    "USA": "\nElectronica 2020 \nBaladas Romanticas",
    "Canada": "\nMix pop 2023 \nRegueton 2020",
    "user1": "\nMusica Clasica \nRock 80's",
    "user2": "\nElectronica 2020 \nBaladas Romanticas",
    "user3": "\nMix pop 2023 \nRegueton 2020",
}

# Clase personalizada para manejar las solicitudes
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/username/'):
            user = self.path[10:]
            if user in usuarios:
                data = {"username": usuarios[user]}
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())  # Codificar la cadena a bytes
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write("País no encontrado.".encode())  # Codificar la cadena a bytes
        else:
            super().do_GET()

# Configuración del servidor
with socketserver.TCPServer(("", 9092), MyHandler) as httpd:
    print("Servidor web en el puerto 9092")
    httpd.serve_forever()
