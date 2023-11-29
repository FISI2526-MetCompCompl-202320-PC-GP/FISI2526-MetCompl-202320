import numpy as np

def ejercicio_1_1_a(n):
  intentos=0
  conteo=0
  while intentos<=n:
    baraja=[]
    carta_numero=0
    while carta_numero<=5:
      carta=np.random.randint(52)
      if carta in baraja:
        carta=np.random.randint(52)
      baraja.append(carta)
      carta_numero+=1
    carta_baraja=2
    pare=False
    conteo_favorable=0
    while carta_baraja<5 and pare==False:
      if (39<=baraja[carta_baraja] and baraja[carta_baraja]<=51):
        carta_baraja+=1
      else:
        pare=True
    if carta_baraja==5:
      conteo+=1
    intentos+=1
  proba=conteo/n
  return proba

print(ejercicio_1_1_a(70000))


def ejercicio_1_1_b(n):
  intentos=0
  conteo=0
  while intentos<=n:
    baraja=[]
    carta_numero=0
    while carta_numero<=4:
      carta=np.random.randint(52)
      if carta in baraja:
        carta=np.random.randint(52)
      baraja.append(carta)
      carta_numero+=1
    carta_baraja=3
    pare=False
    conteo_favorable=0
    while carta_baraja<5 and pare==False:
      if (39<=baraja[carta_baraja] and baraja[carta_baraja]<=51):
        carta_baraja+=1
      else:
        pare=True
    if carta_baraja==5:
      conteo+=1
    intentos+=1
  proba=conteo/n
  return proba

print(ejercicio_1_1_b(50000))

def ejercicio_1_1_c(n):
  intentos=0
  conteo=0
  while intentos<=n:
    baraja=[]
    carta_numero=0
    while carta_numero<=1:
      carta=np.random.randint(52)
      if carta in baraja:
        carta=np.random.randint(52)
      baraja.append(carta)
      carta_numero+=1
    carta_baraja=0
    pare=False
    conteo_favorable=0
    while carta_baraja<=1 and pare==False:
      if (39<=baraja[carta_baraja] and baraja[carta_baraja]<=51):
        carta_baraja+=1
      else:
        pare=True
    if carta_baraja==1:
      conteo+=1
    intentos+=1
  proba=conteo/n
  return proba

print(ejercicio_1_1_c(5000))




