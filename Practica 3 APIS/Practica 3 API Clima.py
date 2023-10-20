import requests

def obtener_ubicacion_geonames(geonames_username, lugar):
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
            print(f"\nInformacion proporcionada por GEONAMES:")
            print(f"Ubicacion Encontrada: {ciudad}, {pais}")
            return ciudad, pais
        else:
            print("Error: Ubicación no encontrada.")
            return None, None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None, None



def obtener_datos_openweather(api_openweather, ciudad, pais):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={api_openweather}"

    try:
        response = requests.get(url)
        data = response.json()
        if "main" in data and "weather" in data:
            temperatura = data["main"]["temp"] - 273.15  # Convertir de Kelvin a Celsius
            condiciones_climaticas = data["weather"][0]["description"]
            print(f"\nInformacion proporcionada por OPENWEATHER:")
            print(f"Temperatura: {temperatura:.2f}°C")
            print(f"Condiciones Climáticas: {condiciones_climaticas}\n")

        else:
            print("Datos meteorológicos no disponibles.\n")
    except Exception as e:
        print(f"Error: {str(e)}")



if __name__ == "__main__":
    #Usuario de Geonames y el lugar que se desee consultar
    geonames_username = "castillo"
    lugar = "Ecatepec de Morelos"
    ciudad, pais = obtener_ubicacion_geonames(geonames_username, lugar)

    if ciudad and pais:
        api_openweather = "152b1599f3e42d9d0f559bf3cf348a2b"
        obtener_datos_openweather(api_openweather, ciudad, pais)

