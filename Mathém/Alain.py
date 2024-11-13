# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 11:15:22 2023

@author: HOME
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 05:52:31 2023

@author: HOME

"""
import numpy as np
import math 
import matplotlib.pyplot as plt
z=np.arange(0,100,0.01)
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
  plt.plot(z,H,label='courbe de H')
  plt.plot(z,V,label='courbe de V')
  plt.xlabel('Axe des x')
  plt.ylabel('Axe des H et V')
  # Ajouter une légende
  plt.legend()
  plt.show()