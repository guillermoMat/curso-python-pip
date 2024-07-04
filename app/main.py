import pandas as pd # type: ignore
import matplotlib.pyplot as plt #type:ignore

def run():
    """
    #dataframe=dataframe[dataframe["Continent"] == "Africa"]
    #el elemento dataframe ahora corresponde solamente a los datos
    #que esten en el contienen de africa

    print("\nMostrando dataframe:")
    print(dataframe)

    #Paises que esten en el continente de africa
    print("\nMostrando Countries: ")
    countries=dataframe["Country/Territory"].values
    print(countries)

    #Porcentaje de poblacion los datos que corresponden a africa
    print("\nMostrando percent:")
    percent=dataframe["World Population Percentage"].values
    print(percent)
    """
    #UNIFICANDO PANDAS CON MATPLOTLIB 
    dataframe=pd.read_csv("population.csv")

    filtrado=dataframe[dataframe["Continent"] == "South America"]
    print("Filtrado 1 (por continente): \n",filtrado)

    #print("Filtrado 2 (por Rank):\n",dataframe[dataframe["Rank"]<100])

    #Integración de PANDAS con MATPLOTLIB
     # Crear el gráfico de torta
    plt.pie(
        filtrado["World Population Percentage"],
        labels=filtrado["Country/Territory"], 
        autopct='%1.1f%%'#se utiliza para mostrar automáticamente los porcentajes en cada porción del gráfico de torta.
    )
    plt.title("Porcentaje de población Sur América")
    plt.xlabel("Países")
    plt.ylabel("Porcentajes")
    plt.savefig("surAmerica.png")     



if __name__ == "__main__":
    run()
