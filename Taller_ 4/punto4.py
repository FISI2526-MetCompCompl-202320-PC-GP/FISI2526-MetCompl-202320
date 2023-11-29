import numpy as np
T=np.array([[0.4,0.25,0.3,0.1],
           [0.2,0.25,0.3,0.1],
           [0.2,0.25,0.1,0.1],
           [0.2,0.25,0.3,0.7]])
#sea pi={A,C,G,T}

pi=np.array([0.25,0,0.5,0.25])
#Para la secuencia del inciso a, tenemos que multiplicar las componentes del vecto correspondiente a la letra con la probabilidad de llegar a la siguiente letra.
probabilidad1=pi[3]*T[3][2]*T[2][1]*T[1][3]*T[3][1]*T[0][0]*T[0][0]*T[0][0]
print('La probabilidad del primer gen es ',(probabilidad1))

Emision=np.array([[0.8,0,0,0.2],
           [0.05,0.9,0.1,0.1],
           [0.05,0.1,0.9,0],
           [0.1,0,0,0.7]])

probabilidad2=probabilidad1*Emision[3][3]*Emision[2][2]*Emision[1][1]*Emision[3][3]*Emision[1][1]*Emision[0][0]*Emision[0][0]*Emision[0][0]
#A cada Letra del segundo gen se le asigna su letra en la misma posición del primer gen, para así escoger la componente de la matriz.
print('La probabilidad del segundo gen a partir del primero es ',(probabilidad2))
           
    



