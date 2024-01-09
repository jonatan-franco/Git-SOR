
import matplotlib.pyplot as plt
import numpy as np


# função para FR

def reforco_0 (comportamento_0):
    return comportamento_0

resp = np.linspace(0.01,10)
taxa_reforcamento_0 = []


# função para VR 

def reforco_1(comportamento):
    return comportamento*1/5
    # B = range, C = 5

b = np.linspace(0.01,10)
taxa_reforcamento = []



# função para VI 

def reforco_2(comportamento):
    return 60 / (6 + 0.5 * (1 / comportamento))
    # T = 60, C = 6

behav = np.linspace(0.01,10)
taxa_reforcamento_2 = []


# função para VT
 
    #'taxa de reforçamento'
reforco_constante = 10 # T/C = 60/6 = 10
    
    #'comportamento'
comp = np.linspace(0.01,10)

    #'para cada valor de comportamento o y será constante'
taxa_reforcamento_3 = [reforco_constante] * len(comp)


# ITERAÇÃO

for resposs in resp:
    taxa_reforcamento_0.append(reforco_0(resposs))

for resposta in b:
   taxa_reforcamento.append(reforco_1(resposta))

for r in behav:
    taxa_reforcamento_2.append(reforco_2(r))

# PLOTS
    
plt.title("Schedules of Reinforcement")
plt.xlabel("Behavior Rate")
plt.ylabel("Reinforcement Rate")
plt.plot(resp, taxa_reforcamento_0, label = "CRF")
plt.plot(b,taxa_reforcamento, label = "VR5")
plt.plot(behav, taxa_reforcamento_2, label = "VI6")
plt.plot(comp, taxa_reforcamento_3, label = "VT10")
plt.legend()
plt.show()

