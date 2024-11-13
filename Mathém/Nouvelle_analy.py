# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 03:41:25 2023

@author: GOHOUEDE Aimé LOick
"""
import numpy as np
import matplotlib.pyplot as plt

t=np.array([0,0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,100])
il=np.arange(0,100,1)  
B=5
ho=1.5
io=0.1
nu= 0.0001
So=B*ho
X=B+(2*ho)
R=So/X
Cw= 0.5
C=R**(1/6)/nu
ip=io
Vo=C*np.sqrt(io*R)
g=9.81
Ho=ho
bo=B

for i in range(len(t)):

      x=10+(12*ho/bo)/(3+(6*ho/bo))
      A=Vo*(Ho*Vo- (Vo-Cw)**2)
      B=2*io*g*Vo -(io*g*x*Vo)+(2*Cw)-(2*Vo)
      G=2*io*g*Ho*Cw+(4*io*g*Ho*Vo)
      z=-Cw*t[i]+il
      H=(Ho-(G/B))*np.exp(-B*z/A)+(G/B)
      
      #print(H)
      plt.plot(il,H,label=f'courbe de H pour t={t[i]}')

      plt.xlabel('Axe de x')
      plt.ylabel(' H et V')
      # Ajouter une légende
      plt.legend()
      plt.show()
                  
