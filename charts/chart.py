import matplotlib.pyplot as plt # type: ignore

def generate_chats():
    labels=["A","B","C"]
    values=[202,120,190]

    fig,ax=plt.subplots()
    ax.pie(values,labels=labels)

    plt.savefig("pie.png")
    plt.close()