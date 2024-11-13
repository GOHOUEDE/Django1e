# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 13:01:35 2023

@author: HOME
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, make_circles
from sklearn.metrics import accuracy_score, log_loss
from tqdm import tqdm

X, y = make_circles(n_samples=100, noise=0.1, factor=0.3, random_state=0)
X = X.T
y = y.reshape((1, y.shape[0]))

print('dimensions de X:', X.shape)
print('dimensions de y:', y.shape)

plt.scatter(X[0, :], X[1, :], c=y, cmap='summer')
plt.show()

def initialisation(dimension):
    parametres={}
    C=len(dimension)
    for c in range (1,C):
    
     parametres [ 'W' +str(c)]= np.random.randn(dimension[c],dimension[c-1] )       
     parametres [ 'b' +str(c)]= np.random.randn(dimension[c],1 )     
  

    return parametres
def forward_propagation(X, parametres):
    C=len(parametres) //2  
    activations = {'A0': X }   
    for c in range (1,C+1):
       
       b= parametres ['b'+str(c)]
       Z=  parametres ['W'+str(c)].dot(activations['A' + str(c-1)])+ b
       activations[ 'A' +str(c)]= 1/(1+np.exp(- Z))

    return activations
def back_propagation(X, y, parametres, activations):
    gradients = {}
    m = y.shape[1]
    C=len(parametres) //2  
    dZ=activations['A'+str(C)]-y

    for c in reversed(range (1,C+1)) :
        A=activations['A'+str(c-1)]
        gradients['dW'+str(c)]=1/m *np.dot(dZ,A.T)
        gradients['db'+str(c)]=1/m* np.sum(dZ, axis=1, keepdims = True)
        if c>1:
          d=parametres ['W'+str(c)]
          dZ=np.dot(d,dZ)*A*(A-1)
    
       
    
    return gradients
def update(gradients, parametres, learning_rate):

  
    C=len(parametres) //2  
    for c in reversed(range (1,C+1)) :
        
       parametres['W'+str(c)] =  parametres['W'+str(c)] -(learning_rate* gradients['dW'+str(c)])
       parametres['b'+str(c)] =  parametres['b'+str(c)] -(learning_rate* gradients['db'+str(c)])

    return parametres


def predict(X, parametres):
    C=len(parametres) //2  
    activations = forward_propagation(X, parametres)
    A2 = activations['A'+str(C)]
    return A2 >= 0.5



def neural_network(X, y, dim=(32,32,32), learning_rate = 0.1, n_iter = 10000):

    # initialisation parametres
    dimensions=list(dim)
    dimensions.insert(0,X.shape[0])
    dimensions.append(y.shape[0])
    
    parametres = initialisation(dimensions)

    train_loss = []
    train_acc = []
    history = []

    # gradient descent
    for i in tqdm(range(n_iter)):
        activations = forward_propagation(X, parametres)
        gradients= back_propagation(X, y, parametres, activations)
        update(gradients, parametres, learning_rate)
        # Plot courbe d'apprentissage
        if i %10 == 0 :     
           C=len(parametres) //2  
           A = activations['A'+str(C)]
           train_loss.append(log_loss(y.flatten(), A.flatten()))
           y_pred = predict(X, parametres)
           train_acc.append(accuracy_score(y.flatten(), y_pred.flatten()))
        
           history.append([parametres.copy(), train_loss, train_acc, i])

        # mise a jour

    # plt.figure(figsize=(12, 4))
    # plt.subplot(1, 2, 1)
    # plt.plot(train_loss, label='train loss')
    # plt.legend()
    # plt.subplot(1, 2, 2)
    # plt.plot(train_acc, label='train acc')
    # plt.legend()
    # plt.show()

    return parametres
    