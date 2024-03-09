import numpy as np
import matplotlib.pyplot as plt
import math as mt

'''
A primeira função gera os esquemas de razão (FR, VR) e o de tempo (VT). 
A segunda função é responsável por criar o esquema de intervalo (VI).
'''



    # funcao 1
    
def feedback(t,n):
    if n == 0:
        return 10
    
    elif n == 1:
        return 5*t # VR
    else:
        return 10*t # FR
    
    
    # funcao 2: VI
    
def feedback_1 (t):
    return 10 * (t/1) ** 0.1



    # variáveis função 1
    
tempo = np.linspace(0,1)
expoente = np.linspace(0,1,3)  
reforco = []

    # variáveis funçãoo 2

tempo1 = np.linspace(0,1)
reforco1 = []
    

    # iteração
def get_legenda(expoente):
    if expoente == 0:
        return f'VT expoente = {0}'
    elif expoente == 1:
        return f'VR expoente = {1}'
    elif expoente == 0.1:
        return f'VI expoente = {0.1}'
    else:
        return f'FR expoente = {1}'
    
print(expoente)

for e in expoente:  
    reforco = []  
    for t in tempo:
        # print(e,t)
        reforco.append(feedback(t,e))   
    plt.plot(tempo, reforco, label = get_legenda(e))
    reforco = []


for time in tempo1:
        # print(e,t)
    reforco1.append(feedback_1(time))
plt.plot(tempo1,reforco1, label = get_legenda(0.1))
reforco1 = []

# PLOTS


plt.legend()
plt.title("Feedback Function")
plt.xlabel('Allocation of Time (t/T)')
plt.ylabel('Reinforcers obtained during T (R)')
plt.show()
        