import requests
import typer
from dotenv import load_dotenv
import os
import csv
import json

# Inicializar la aplicación de Typer
app = typer.Typer()

# Cargar la API key desde el archivo .env
load_dotenv()
api_key = os.getenv("api_key")

# Función principal que acepta la ciudad, el país y el formato de salida como argumentos
@app.command()
def obtener_clima(
    ciudad: str, 
    pais: str, 
    formato: str = typer.Option("json", help="Formato de salida: json, csv, texto")):

    #URL de la API
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&lang=es&units=metric&appid={api_key}"

    # solicitud a la API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Filtros: obtener la información que queremos
        temperatura = data["main"]["temp"]
        humedad = data["main"]["humidity"]
        viento = data["wind"]["speed"]

        # Crear un diccionario con los datos
        clima_data = {
            "ciudad_Pais": ciudad,
            "pais": pais,
            "temperatura": temperatura,
            "humedad": humedad,
            "viento": viento
        }

        # Mostrar la salida según el formato seleccionado
        if formato == "json":
            print(json.dumps(clima_data, ensure_ascii=False, indent=4))
        elif formato == "csv":
            # Crear el CSV como texto
            print("ciudad,pais,temperatura,humedad,viento")
            print(f"{ciudad},{pais},{temperatura},{humedad},{viento}")
        elif formato == "texto":
            print(f"La temperatura en {ciudad} es de {temperatura}°C, la humedad es del {humedad}% y el viento es de {viento} km/h.")
        else:
            print("Formato no soportado. Usa 'json', 'csv' o 'texto'.")
    else:
        print(f"Error al obtener los datos de la API: {response.status_code}")


if __name__ == "__main__":
    app()
