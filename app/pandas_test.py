import pandas as pd #type:ignore

#Manipulacion y analisis de datos.

#Estructuras de datos
#Serie y DataFrame

#SERIE --- Matriz unidimensional
unidimensional=[5,8,6,7,2,4]
#DataFrame --- Bidimensional 
bidimensional={
    "name":["carlos","alicia","eliana","emiliano"],
    "age":[22,36,29,35],
   "city": ["Posadas","Chaco","Entre Ríos","Santa fe"]
}

#Transformacion
serie=pd.Series(unidimensional)
#quedaria una tabla de 2 columnas, una corresponde al indice y la segunda a los datos
print("\nMostrando tipo que es serie: ",type(serie))#es tipo pandas.serie
print("\nMostrando SERIE:\n",serie)

dataframe=pd.DataFrame(bidimensional)#esto queda como una tabla de BD
print("\nMostrando tipo que es dataframe: ",type(dataframe))#es tipo pandas.dataframe
print("\nMostrando DATAFRAME:\n",dataframe)
print("*****"*4)
print()

#Probando manipulacion del dataframe

print("Mostrando por columna")
print(dataframe["city"])
print("\nMostrando fila por indice")
print(dataframe.loc[0])
print("\nMostrando con una condicion (edad menor a 30)")
condicion=dataframe[dataframe["age"]<30]
print(condicion)
