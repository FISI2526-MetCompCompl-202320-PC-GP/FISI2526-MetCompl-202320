import numpy as np
T=np.array([[0.4,0.25,0.3,0.1],
           [0.2,0.25,0.3,0.1],
           [0.2,0.25,0.1,0.1],
           [0.2,0.25,0.3,0.7]])
#sea pi={A,C,G,T}

pi=np.array([0.25,0,0.5,0.25])
#Para la secuencia del inciso a, tenemos que multiplicar las componentes del vecto correspondiente a la letra con la probabilidad de llegar a la siguiente letra.
probabilidad=pi[3]*T[3][2]*T[2][1]*T[1][3]*T[3][1]*T[0][0]*T[0][0]*T[0][0]
print(probabilidad)



