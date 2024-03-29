import requests

def procesar_respuestas(endpoint, num_vehiculo):

    try:
        request = requests.get(endpoint)
        status_code = request.status_code
        print(f"La API respondio con el codigo {status_code}")

        response = request.json()
        print(f"Candidad de vehiculos: {len(response)}")

        print(f"Caracteristicas del vehiculo seleccionado {response[num_vehiculo]}")

    except requests.JSONDecodeError:
        print("No se pudo procesar la respuestade la peticion JSON")
    except IndexError:
        print("Se esta tratando de acceder a un vehiculo que no esta en la lista")
    except Exception as e:
        print("Se levanto una Excepcion")
        print(e)
    else:
        print("No ocurrion ninguna error")
    finally:
        print("Se termino el proceso")

    endpoint_ok = "https://run.mocky.io/v3/..."
    endpoint_not_found = "https://run.mocky.io/v3/..."

    procesar_respuestas(endpoint=endpoint_ok, num_vehiculo=1)
    procesar_respuestas(endpoint=endpoint_not_found, num_vehiculo=1)
