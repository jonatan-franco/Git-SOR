import numpy as np
import matplotlib.pyplot as plt



# FUNÇÃO

def feed(t,n):
    if n == 0 and t == 0:
        return 20
    else:
        return 20*(t/10)**n
        
# VARIÁVEIS

time_operante = np.arange(0, 10,0.1)
expoente = np.arange(0, 1,0.02)
reforco = []


# ITERAÇO

for e in expoente:
    for t in time_operante:
        print(f"expoente: {e} |" , f"tempo: {t}")
        reforco.append(feed(t,e))       
    
    plt.plot(time_operante, reforco)
    reforco = []
   
   
# PLOTS
 
plt.title("Função de Feedback")
plt.xlabel('Tempo')
plt.ylabel('Reforco')
plt.show()
        
