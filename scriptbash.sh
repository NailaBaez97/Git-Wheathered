#!/bin/bash

set -e 

mv .env.sample .env

python -m venv venv 

.venv/Scripts/Activate 

#Este comando le pide al usuario que ingrese su clave de API.
read -p "Ingresa tu API key: " api_key 
echo "API_KEY='${api_key}'" >> .env