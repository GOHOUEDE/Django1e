# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 05:52:31 2023

@author: HOME

"""
import numpy as np
import math 
import matplotlib.pyplot as plt
z=np.arange(0,100,1)
D=np.array([5])
io=0.1
ho=1.5
nu=0.03
g=9.8
Ho=ho


for i in range(len(D)):
  beta=1-(2*ho/D[i])
  bo=D[i]*np.sqrt(1-beta**2)
  R=D[i]/4*(1-(beta*np.sqrt(1-beta**2)/math.acos(beta)))
  Cw=R**(1/6)/nu
  x=10+(12*ho/bo)/(3+(6*ho/bo))
  vo=Cw*np.sqrt(io*R)

  a=Cw-vo
  b=2*Cw-(x*vo)
  A=2*(a*Ho)-(ho*vo)/b
  B=Ho-A
  c=-1*g*io*b/(vo*g*ho-a**2)
  C=np.exp(c*z)
  H=A+(B*C)
  
  V=1/ho*a*(H-Ho)+vo
  #print(H)
  plt.plot(z,H,label='courbe de H pour t=0')
  plt.plot(z,V,label='courbe de V pour t=0')
  plt.xlabel('Axe de z')
  plt.ylabel(' H et V')
  # Ajouter une légende
  plt.legend()
  plt.show()
n=len(V) 
Hau=np.zeros((10,n))
Vit=np.zeros((10,n))
Hau[0,:]=H
Vit[0,:]=V 
r=1
a=2
b=2
ip=0.05
dt=1
for i in range(9):
    for j in range(n-1):
    
      Hau[i+1][j]=Hau[i][j]-(r*Vit[i][j]*(Hau[i][j+1]-Hau[i][j]))-((a/b)*r*(Vit[i][j+1]-Vit[i][j]))
      Vit[i+1][j]=Vit[i][j]-(g*r*(Hau[i][j+1]-Hau[i][j]))-(r*Vit[i][j]*(Vit[i][j+1]-Vit[i][j]))+(dt*g*(io-ip))
      # plt.plot(z,Hau[i+1])                                                         
      # plt.plot(z,Vit[i+1])  
      # plt.show()
      
for i in range(9):   
      plt.plot(z,Hau[i+1],label=f'courbe de H pour t={i+1}')                                                         
      plt.plot(z,Vit[i+1],label=f'courbe de V pour t={i+1}')  
      plt.xlabel('Axe de z')
      plt.ylabel(' H et V')
      plt.legend()
      plt.show()