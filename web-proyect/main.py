import store
from fastapi import FastAPI 


def call_store():
    store.get_categories()

app=FastAPI()

@app.get("/")
def get_list():
    return [5,4,8,2,3]

@app.get("/contact")
def get_contacts():
    return {
        "name":"guille",
        "age":21,
        "email":"gm32@yahoo.com"
    }

#uvicorn main:app --reload
#uvicorn libreria que viene con fastapi (antes se instalaba a parte de fastapi, osea las dos juntas)
#main---es el archivo 
#app---la carpeta o aplicacion
#--reload --- es para que recargue la pagina cuando hago alguna modificacion en codigo
if __name__ == "__main__":
    call_store()

