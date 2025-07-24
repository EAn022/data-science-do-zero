from matplotlib import pyplot as plt

x = [1991,1992,1993,1994]
y = [1, 2, 3, 4]

plt.plot(x,y,color='green',marker='o',linestyle='solid' )
plt.title("ovocelente")
plt.ylabel("ovaldo")
plt.savefig("grafico.png")