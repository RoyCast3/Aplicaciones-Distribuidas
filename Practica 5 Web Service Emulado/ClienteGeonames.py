import requests

# URL del servidor web (asegúrate de que la dirección y el puerto coincidan)
url_base = 'http://localhost:9090'

def obtener_temperatura(estado):
    url = f'{url_base}/location/{estado}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return f'Ubicacion Encontrada: {data["location"]:}, {estado}'
    elif response.status_code == 404:
        return f'Ubicacion no Encontrada: {estado}'
    else:
        return f'Error en la solicitud: Código {response.status_code}'

# Ejemplos de uso
estadoes = ["Mexico", "Alberta", "Quebec", "Florida"]
for estado in estadoes:
    resultado = obtener_temperatura(estado)
    print(resultado)
