import requests

#POST --- Crear un nuevo recurso

# URL de la API
url = 'https://jsonplaceholder.typicode.com/posts'

# Datos a enviar en la solicitud POST
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Headers personalizados
headers = {
    'Content-Type': 'application/json; charset=UTF-8'
}

# Realizar la solicitud POST
response = requests.post(url, json=data, headers=headers)

# Verificar y mostrar la respuesta
print(response.status_code)
print(response.json())
