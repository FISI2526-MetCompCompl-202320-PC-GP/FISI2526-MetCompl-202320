import numpy as np
def normalizacion(v):
  suma=0
  for i in v:
     suma+= (i[0])**2
  norma=(suma**0.5)
  if norma==0:
      return v
  else:
    vector_normal=v/norma
    return vector_normal

def tres(A,v_o):
  A=A
  iteracion_maxima=10000
  iteracion=0
  while iteracion<iteracion_maxima:
      v=A.dot(v_o)
      v= normalizacion(v)
      v_o=v
      iteracion+=1
  return v

matriz=np.array([[-2,1,0],[1,-2,1],[0,1,-2]])
vector0=np.array([[1],[1],[900]])
respuesta_01=tres(matriz,vector0)
Valor=((matriz.dot(respuesta_01))[0])/(vector0[0])
print("El menor valor es de "+str(Valor*2))