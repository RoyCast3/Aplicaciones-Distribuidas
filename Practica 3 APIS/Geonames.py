#TAREA: Utiliza la respuesta de la API de Geonames (Ubicación) 
#       como entrada para la API de OpenWeatherMap (Datos meteorológicos) 
#       y que se despliegue en pantalla

import requests
def obtener_informacion_ubicacion(geonames_username, lugar):
    url = f"http://api.geonames.org/searchJSON?name={lugar}&maxRows=1&username={geonames_username}"

    try:
        #Almacena el http con la info que le pide
        response = requests.get(url)
        #Guardar la informacion en un json
        data = response.json()

        if "geonames" in data and data["geonames"]:
            #Obtiene las variables a manera de simular una tabla
            ubicacion = data["geonames"][0]
            ciudad = ubicacion['name']
            pais = ubicacion['countryCode']
            return ciudad, pais
        else:
            print("Ubicación no encontrada.")
            return None, None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None, None

def obtener_datos_meteorologicos(api_key, ciudad, pais):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()
        if "main" in data and "weather" in data:
            temperatura = data["main"]["temp"] - 273.15  # Convertir de Kelvin a Celsius
            #condiciones_climaticas = data["weather"][0]["description"]

            print(f"Nombre: {ciudad}")
            print(f"Pais: {pais}")
            print(f"Temperatura en {ciudad}, {pais}: {temperatura:.2f}°C")
            
            #print(f"Condiciones Climáticas en {ciudad}, {pais}: {condiciones_climaticas}")

        else:
            print("Datos meteorológicos no disponibles.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    #tu_usuario_de_geonames
    geonames_username = "castillo" #tu usuario en geoname
    lugar = "Sinaloa"  # Cambia esto a la ubicación que desees consultar
    ciudad, pais = obtener_informacion_ubicacion(geonames_username, lugar)

    if ciudad and pais:
        #tu_api_key_de_openweathermap
        api_key = "152b1599f3e42d9d0f559bf3cf348a2b"
        obtener_datos_meteorologicos(api_key, ciudad, pais)
