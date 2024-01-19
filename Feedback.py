import numpy as np
import matplotlib.pyplot as plt


'''
A primeira função gera os esquemas de razão (FR, VR) e o de tempo (VT). 
A segunda função é responsável por criar o esquema de intervalo (VI).
'''



    # funcao 1
    
def feedback(t,n):
    if n == 0:
        return 10
     
    else:
        return 10 * (t/1) ** 1 / n
    
    
    # funcao 2 
    
def feedback_1 (t):
    return 10 * (t/1) ** 0.058



    # variáveis função 1
    
tempo = np.linspace(0,1)
expoente = np.arange(3)    
reforco = []

    # variáveis funçãoo 2

tempo1 = np.linspace(0,1)
reforco1 = []
    

    # iteração



def get_legenda(expoente):
    if expoente == 0:
        return 'VT10'
    elif expoente == 1:
        return 'FR10'
    elif expoente == 2:
        return 'VR5'
    else:
        return f'expoente = {expoente:.2f}'

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
plt.plot(tempo1,reforco1, label = "VI")
reforco1 = []

# PLOTS


plt.legend()
plt.title("Feedback Function")
plt.xlabel('Allocation of Time (t/T)')
plt.ylabel('Reinforcers obtained during T (R)')
plt.show()
        