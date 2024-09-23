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

if __name__ == "__main__":
    app()
