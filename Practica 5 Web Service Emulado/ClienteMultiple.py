import requests

# URL del servidor web (asegúrate de que la dirección y el puerto coincidan)

url_Geonames = 'http://localhost:9090'
url_CLima = 'http://localhost:9091'
url_Spotify = 'http://localhost:9092'



def obtener_temperatura(pais):
    url = f'{url_CLima}/temperature/{pais}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return f'Temperatura en {pais}: {data["temperature"]:.2f}°C'
    elif response.status_code == 404:
        return f'País no encontrado: {pais}'
    else:
        return f'Error en la solicitud: Código {response.status_code}'

def obtener_playlist(user):
    url = f'{url_Spotify}/username/{user}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f'Playlist más escuchada en {user}: {data["username"]:}\n'
    elif response.status_code == 404:
        return f'Usuario no encontrado: {user}\n'
    else:
        return f'Error en la solicitud: Código {response.status_code}'
    
def obtener_ubicacion(estado):
    url = f'{url_Geonames}/location/{estado}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        pais = data["location"]
        print(pais)
        print(obtener_temperatura(pais))
        print(obtener_playlist(pais))
        return f'Ubicacion Encontrada'
    elif response.status_code == 404:
        return f'Ubicacion no Encontrada: {estado}'
    else:
        return f'Error en la solicitud: Código {response.status_code}'

# Ejemplos de uso
estado = input('Ingresa una ciudad de América: ')
resultadoGeonames = obtener_ubicacion(estado)