import requests

url = 'http://127.0.0.1:8000/predict'

# Lista con diferentes medidas para probar qué nos devuelve el modelo
muestras = [
    {"input": [5.1, 3.5, 1.4, 0.2]},  # Típicamente clase 0
    {"input": [6.0, 2.9, 4.5, 1.5]},  # Típicamente clase 1
    {"input": [6.9, 3.1, 5.1, 2.3]}   # Típicamente clase 2
]

print("Iniciando pruebas del modelo...\n")

for i, muestra in enumerate(muestras):
    respuesta = requests.post(url, json=muestra)
    datos_respuesta = respuesta.json()
    
    print(f"Muestra {i+1}: {muestra['input']}")
    print(f"-> Predicción del modelo: Clase {datos_respuesta.get('prediction')}\n")