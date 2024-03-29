#documentacion en: docs.python-requests.org
#Peticiones HTTP GET POST PUT DELETE
#HTTP usa protocolo para transferir datos y la comunicacion entre servicios
#intalar libreria "request": pip install requests
import requests

response = requests.get('https://api.github.com')
print(response.headers)
print(response.content) #regresa en bites, la respuesta empieza con "b"
print(response.status_code)# regresa el status del codigo. si es 200 esta bien
print(response.headers)# regresa la info en string
print(response.json())# regresa la info en diccionarios
# print(response.json()["valor a buscar"])# busca los valores especificos 

#podemos buscar info de una pagina en especifico

git_response = requests.get(
    "https://github.com/search/repositories",
    params={'q':'python'} # q significa query, params es para filtrar info
)
print(git_response.json())

data = git_response.json() #se guarda el json de la respuesta en una variable
print(data.keyes())#se llama la variable y pedimos solo el valor de las llaves con el metodo keyes()


#sintaxis: nombreVariable = requests.get("url")
#nomVariable = request.post("url", data=("key":"value"))
#nomVar = request.put("url", data=("key":"value"))
#for delete, head and options, is same get sintax

#API (Interfaz de Programacion de Aplicaciones)
#usa Funciones y Protocolos y metodos HTTP
#Tiene Endpoint

#POST envia informacion de una base de datos que esta ligada a un servidor

url = 'https://webhook.site/9fdd49d6-8a20-4a32-94bc-c76000754136'
payload = {'plato': 'Pasta', 'cantidad': 2}
query_params = {'nombre': 'Pancho'}
comida_response = requests.post(url, data=payload, params=query_params)
print(comida_response.json())