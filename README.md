GIT-WEATHERED 🌤️
Tu prónostico a Comandos

Desarrollo de una aplicación CLI que consulte una API de clima y muestre la información climática en la terminal.

Características:
-Consulta del clima en tiempo real.
-Formatos de salida: JSON, CSV o texto plano.

Datos proporcionados:
-Ciudad y país.
-Temperatura humedad y viento.
-Fecha de última actualización.

Uso:

Clima en formato texto (predeterminado): python script.py "Ciudad" "Pais"

Clima en formato JSON: python script.py "Ciudad" "Pais" --formato json

Requisitos:
Librerías: requests, Typer,  load_dotenv, os, csv, JSON.
Clave API de WeatherAPI en API_KEY.py.

Resumen:

Esta versión inicial permite consultar el clima actual de cualquier ciudad utilizando datos de WeatherAPI. La aplicación devuelve información como temperatura humedad y viento. Se puede obtener la salida en formato JSON, CSV O texto plano.

