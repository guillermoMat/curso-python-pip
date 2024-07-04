import requests

#   https://fakeapi.platzi.com/
def get_categories():
    r=requests.get("https://api.escuelajs.co/api/v1/categories")
    print("Estado: ",r.status_code)
    contenido=r.text
    print("Tipo de contenido: ",type(contenido))
    
    #print("\nContenido:\n",r.text)
    # muestra todo el contenido completo con formato lista
    # con diccionarios, pero el tipo de dato oficial es STR

    #Convertir el tipo STR a JSON
    print("\nFormato JSON: ")
    categories=r.json()

    #algo extra, solo para mostrar los primeros 5 elementos
    # ya que son muchos
    myList=categories[:4]
    #print(myList)
    
    for item in myList:
        print(item)
        print("*****"*5)
    """
    #Otra forma de mostrar por indice
    for i in myList:
        print(i["name"],i["id"])
        print("*****"*5)
    """