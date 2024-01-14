import matplotlib.pyplot as plt
import numpy as np


# FUNÇÃO

expoente = np.arange(0.1, 1.1, 0.1)

def feed(t,n):
    return 60 * (t/100-t) ** n
        # maximo de reforço = 60
        
# VARIAVEIS

tempo_operante = np.arange(0, 100)

reforco = []

# ITERAR

for e in expoente:
    for i in tempo_operante:
        reforco.append(feed(e,i))
    plt.plot(tempo_operante, reforco, label = f'Expoente {e}' )
    reforco = []

# plt.legend()    


plt.title("Feedback Function")
plt.xlabel("Tempo total")
plt.ylabel("Reforço")
plt.show()
