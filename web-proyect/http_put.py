import requests

#PUT --- Actualizar

# URL de la API (con el ID del recurso a actualizar)
url = 'https://jsonplaceholder.typicode.com/posts/1'

# Datos a enviar en la solicitud PUT
data = {
    'id': 1,
    'title': 'foo_updated',
    'body': 'bar_updated',
    'userId': 1
}

# Headers personalizados
headers = {
    'Content-Type': 'application/json; charset=UTF-8'
}

# Realizar la solicitud PUT
response = requests.put(url, json=data, headers=headers)

# Verificar y mostrar la respuesta
print(response.status_code)
print(response.json())
