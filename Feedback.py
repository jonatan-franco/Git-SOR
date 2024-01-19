import numpy as np
import matplotlib.pyplot as plt



# def feed_intervalo(t):
#     return 10*(t/1)**1

# time_operante = np.linspace(0,1)
# reforco = []


def feedback(t,n):
    if n == 0:
        return 10
    # elif 0 < n < 1:
    #     return 10 * (t/1) ** 1 / n     
    else:
        return 10 * (t/1) ** 1 / n
    
    
tempo = np.linspace(0,1)
expoente = np.arange(4)    
reforco = []


def feedback_1 (t):
    return 10 * (t/1) ** 0.058

# c = range(0,5)
tempo1 = np.linspace(0,1)
# expoente1 = np.arange(3)
# variavel = np.arange(2)

reforco1 = []


    

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





# def feed_intervalo_1(t):
#     return 10*(t/1)**0.0558

# time_operante_1 = np.linspace(0,1)
# r = [] 


# def feed_intervalo_2(t):
#     return 10*(t/1)**0

# time_operante_2 = np.linspace(0,1)
# r2 = [] 


# def feed_intervalo_3(t):
#     return 10*(t/1)//5

# time_operante_3 = np.linspace(0,1)
# r3 = []


# for tempo in time_operante:
#     reforco.append(feed_intervalo(tempo))
# plt.plot(time_operante, reforco)
# reforco = []

# for ti in time_operante_1:
#     r.append(feed_intervalo_1(ti))
# plt.plot(time_operante_1, r)
# r = []


# for time in time_operante_2:
#     r2.append(feed_intervalo_2(time))

# plt.plot(time_operante_2, r2)
# r2 = []

# for time1 in time_operante_3:
#     r3.append(feed_intervalo_3(time1))

# plt.plot(time_operante_3, r3)
# r3 = []
  
  
  
  
  
plt.title("Função de Feedback")
plt.xlabel('Tempo')
plt.ylabel('Reforco')
plt.show()
        