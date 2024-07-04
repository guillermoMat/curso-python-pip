import requests

#DELETE --- eliminar

# URL de la API (con el ID del recurso a eliminar)
url = 'https://jsonplaceholder.typicode.com/posts/1'

# Realizar la solicitud DELETE
response = requests.delete(url)

# Verificar y mostrar la respuesta
print(response.status_code)
