import requests

API_KEY = "c279bc7c-e59d-4464-8fac-3be0de31e4bd"

def geocodificar(ciudad):
    url = "https://graphhopper.com/api/1/geocode"
    params = {
        "q": ciudad,
        "locale": "es",
        "key": API_KEY
    }
    respuesta = requests.get(url, params=params)
    datos = respuesta.json()
    if datos["hits"]:
        punto = datos["hits"][0]["point"]
        return punto["lat"], punto["lng"]
    return None, None

def calcular_ruta(origen, destino, vehiculo):
    lat1, lng1 = geocodificar(origen)
    lat2, lng2 = geocodificar(destino)

    if not lat1 or not lat2:
        print("No se pudo encontrar alguna ciudad.")
        return

    url = "https://graphhopper.com/api/1/route"
    params = {
        "point": [f"{lat1},{lng1}", f"{lat2},{lng2}"],
        "vehicle": vehiculo,
        "locale": "es",
        "instructions": "true",
        "key": API_KEY
    }
    respuesta = requests.get(url, params=params)
    datos = respuesta.json()

    if "paths" in datos:
        ruta = datos["paths"][0]
        distancia_km = ruta["distance"] / 1000
        distancia_millas = distancia_km * 0.621371
        tiempo_ms = ruta["time"]
        horas = tiempo_ms // 3600000
        minutos = (tiempo_ms % 3600000) // 60000

        print(f"\n===== RESULTADO DEL VIAJE =====")
        print(f"Origen      : {origen}")
        print(f"Destino     : {destino}")
        print(f"Vehículo    : {vehiculo}")
        print(f"Distancia   : {distancia_km:.2f} km / {distancia_millas:.2f} millas")
        print(f"Duración    : {horas}h {minutos}min")
        print(f"\n--- Narrativa del viaje ---")
        for instruccion in ruta["instructions"]:
            print(f"  → {instruccion['text']}")
    else:
        print("Error al calcular la ruta:", datos)

while True:
    print("\n===== CALCULADORA DE VIAJE CHILE-PERÚ =====")
    origen = input("Ciudad de Origen (o 's' para salir): ")
    if origen.lower() == 's':
        print("Saliendo...")
        break

    destino = input("Ciudad de Destino: ")

    print("\nTipo de transporte:")
    print("1. car (auto)")
    print("2. bike (bicicleta)")
    print("3. foot (a pie)")
    opcion = input("Elige (1/2/3): ")

    vehiculos = {"1": "car", "2": "bike", "3": "foot"}
    vehiculo = vehiculos.get(opcion, "car")

    calcular_ruta(origen, destino, vehiculo)
