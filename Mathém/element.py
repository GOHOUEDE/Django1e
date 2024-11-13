# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 06:15:14 2023

@author: HOME
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
a=-1
b=1
alpha=1
n=198
x=np.linspace(-100,100,200)
hx=x[2]-x[1]
Re=np.matrix('1,-1;-1,1')
Me=np.matrix([[2,1],[1,2]])
Re=alpha/hx*Re
Me=hx/6*Me
K=np.zeros(200)
R=np.zeros((198,198))
M=np.zeros((198, 198))

for k in range(n-1):

      for i in range(2):
           for j in range(2):
               I=k+i
               J=k+j
               R[I,J]= R[I,J]+Re[i,j]
               M[I,J]= M[I,J]+Me[i,j]
# Définition de la fonction à 


F=np.ones(198)

     
for i in range(198):
    def f(y):
        r=x[i+1]
        c=x[i]-x[i+1]
        #return x
        return (y-r)/(c)*y**2
     # Calcul de l'intégrale de f(x) de 0 à 1
    Fc= integrate.quad( f, x[i-1], x[i+1] )
    F[i]=Fc[0]
               
#F=x[1:199]**2-3*               
#F=x[1:199]**2-3*

U=np.linalg.inv(R-M)  
   
U=np.dot(U,F)  

K[0]=0
K[199]=0
for i in range(198):
    K[i+1]=U[i]
    
     
plt.plot(x,K)
# c=1
# d=1
# #y=x**2 -1
#y=c*np.exp(-x)+d*np.exp(x)+x**2+2
#plt.plot(x,y)
#plt.show