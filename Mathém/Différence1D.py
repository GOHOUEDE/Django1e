# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 17:31:16 2023

@author: HOME
"""

import numpy as np
import math 
import matplotlib.pyplot as plt
t=np.array([0,0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8])
dt=0.1
tf=2
t=np.arange(0,tf,dt)
x0=-10
x1=10
dx=0.2
il=np.arange(x0,x1,dx)
 
g=9.81
io=0.001
ip=0.005






V=(il)
H=(il-4)**2
  
n=len(V)
m=len(t) 
Hau=np.zeros((m,n))
Vit=np.zeros((m,n))
Hau[0,:]=H
Vit[0,:]=V 
r=dt/dx
a=2
b=2
ip=0.05
dt=0.2
for i in range(9):
    for j in range(n-1):
    
      Hau[i+1][j]=Hau[i][j]-(r*Vit[i][j]*(Hau[i][j+1]-Hau[i][j]))-((a/b)*r*(Vit[i][j+1]-Vit[i][j]))
      Vit[i+1][j]=Vit[i][j]-(g*r*(Hau[i][j+1]-Hau[i][j]))-(r*Vit[i][j]*(Vit[i][j+1]-Vit[i][j]))+(dt*g*(io-ip))
      # plt.plot(z,Hau[i+1])                                                         
      # plt.plot(z,Vit[i+1])  
      # plt.show()
      
for i in range(9):   
      plt.plot(il,Vit[i],label=f'courbe de H pour t={i}')                                                         
   
      plt.xlabel('Axe de z')
      plt.ylabel(' H ')
      plt.legend()
plt.show()   

      
for i in range(9):   
                                                           
      plt.plot(il,Vit[i],label=f'courbe de V pour t={i}')  
      plt.xlabel('Axe de z')
      plt.ylabel(' V')
      plt.legend()
plt.show()   