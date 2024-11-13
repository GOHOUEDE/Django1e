# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 20:55:12 2023

@author: Romaric
"""

import numpy as np
import matplotlib.pyplot as plt

#  Paramètres et initialisation 

i0=0.001
ip=0.005
import math 

#Conditions initiales 
H0=1.5


g= 9.81
dt=0.2
dx=0.4
r= dt/dx
Nt=10
Nx=10
a=10
b=8
D=5
nu=0.03

# Vecteurs Initialisation
H=np.zeros(Nx,dtype=float)
V=np.zeros(Nx,dtype=float)

Hs=np.empty((Nx,Nx))
Vs=np.empty((Nx,Nx))

#Schémas 
for n in range(Nt-1):
    H_i=np.copy(H)
    V_i=np.copy(V)
    
    
    for i in range(Nx-1):
        if(n==0):
            beta=1-(2*H0/D)
            bo=D*np.sqrt(1-beta*2)
            R=D/4*(1-(beta*np.sqrt(1-beta**2)/math.acos(beta)))
            Cw=R**(1/6)/nu
            x=10+(12*H0/bo)/(3+(6*H0/bo))
            vo=Cw*np.sqrt(i0*R)
            
            a=Cw-vo
            b=2*Cw-(x*vo)
            A=2*(a*H0)-(H0*vo)/b
            B=H0-A
            c=-1*g*i0*b/(vo*g*H0-a**2)
            C=np.exp(c*(i/Nx))
            H_i[i]=A+(B*C)
            V_i[i]=1/H0*a*(H_i[i]-H0)+vo
            
            H[i]=H_i[i]
            V[i]=V_i[i]
        

            
        else:
            H_i[i]= H[i] - (r)*((V[i]*(H[i+1]-H[i]))-(a/b)*r*(V[i+1]-V[i]))
            V_i[i]= V[i]- (r)*(V[i]*(V[i+1]-V[i])) - (g*r)*(H[i+1]-H[i]) +dt*g*(i0 -ip)
            H=H_i
            
            
        
        print(H_i[i],V_i[i])
        Hs[n,:]=H_i
        Vs[n,:]=V_i
        
 #Visualisation de l'évolution de la section transversale (A) au fil du temps      
for ii in range(0):
    plt.plot(Hs[ii,:], label=f"ligne{ii+1}")
    
#plt.legend()
plt.xlabel('Position')
plt.ylabel('Section Transversale X')
plt.title('Évolution de la Section Transversale au Fil du Temps')
plt.grid(True)    
plt.show()


# Visualisation de l'évolution de la vitesse (u) au fil du temps
plt.figure(figsize=(10, 6))
for ii in range(Hs.shape[0]):
    plt.plot(Vs[ii,:], label=f"ligne{ii+1}")
    
plt.xlabel('Position')
plt.ylabel('Vitesse (u)')
plt.title('Évolution de la Vitesse au Fil du Temps')
plt.grid(True)
plt.show()
    
    
   
        
   
    
        
    

    







