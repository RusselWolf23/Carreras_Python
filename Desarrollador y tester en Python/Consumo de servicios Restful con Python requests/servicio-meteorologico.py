# Este programa hace una petición al servicio web para obtener los datos de temperatura de una ciudad
import os
import requests

# Obtenemos la clave API de nuestra cuenta Open Weather almacenada en una bariable de entorno
apy_key= os.getenv('open_weather_api_key')

# Pedimos el nombre de la ciudad y pasamos los datos como una 
ciudad=input("Dé qué ciudad quieres saber la información meteorológica?")
parametros={"q":ciudad, "appid":apy_key}
r=requests.get("https://api.openweathermap.org/data/2.5/weather",params=parametros)

if r.status_code == 200:
    datos=r.json()
    temp=float(datos["main"]["temp"])-273.15
    print(f"Temperatura de {ciudad} es de ","{:.2f}".format(temp),"ºC", sep="")
else:
    print("La petición no es correcta")
