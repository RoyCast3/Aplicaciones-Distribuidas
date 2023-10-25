import requests

# URL del servidor web (asegúrate de que la dirección y el puerto coincidan)
url_base = 'http://localhost:9092'

def obtener_temperatura(user):
    url = f'{url_base}/username/{user}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return f'Playlist de {user}: {data["username"]:}\n'
    elif response.status_code == 404:
        return f'Usuario no encontrado: {user}\n'
    else:
        return f'Error en la solicitud: Código {response.status_code}'

# Ejemplos de uso
users = ["user1", "user2", "user3", "user4"]
for user in users:
    resultado = obtener_temperatura(user)
    print(resultado)
