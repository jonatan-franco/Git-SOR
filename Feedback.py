import numpy as np
import matplotlib.pyplot as plt


'''
A primeira função gera os esquemas de razão e o de tempo (VT). 
A segunda função é responsável por criar o esquema de intervalo (VI).
'''



    # funcao 1
    
def feedback(t,n):
    if n == 0:
        return 10
    # elif 0 < n < 1:
    #     return 10 * (t/1) ** 1 / n     
    else:
        return 10 * (t/1) ** 1 / n
    
    
    # funcao 2 
    
def feedback_1 (t):
    return 10 * (t/1) ** 0.058



    # variáveis função 1
    
tempo = np.linspace(0,1)
expoente = np.arange(4)    
reforco = []

    # variáveis funçãoo 2

tempo1 = np.linspace(0,1)
reforco1 = []
    

    # iteração

for e in expoente:  
    reforco = []  
    for t in tempo:
        # print(e,t)
        reforco.append(feedback(t,e))
    plt.plot(tempo,reforco)
    reforco = []


for time in tempo1:
        # print(e,t)
    reforco1.append(feedback_1(time))
plt.plot(tempo1,reforco1)
reforco1 = []

# PLOTS

plt.title("Função de Feedback")
plt.xlabel('Tempo')
plt.ylabel('Reforco')
plt.show()
        