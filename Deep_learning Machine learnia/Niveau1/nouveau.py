# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 14:50:11 2023

@author: HOME
"""


import numpy as np
import matplotlib.pyplot as plt 
from sklearn.datasets import make_blobs
from sklearn.metrics import accuracy_score
from tqdm import tqdm

X,y=make_blobs(n_samples=100,n_features=2,centers=2,random_state=0)
#new=np.array([-1,6])

#print(X)
y= y.reshape((y.shape[0],1))      #(2,1)
print('dimension de X :',X.shape) 
print('dimension de Y :',y.shape)

plt.scatter(X[:,0],X[:,1],c=y,cmap='summer')
#plt.scatter(new[0],new[1],c='r')
plt.show()

def initialiser (X):
      W=np.random.randn(X.shape[1],1)   # (2,1)
      b=np.random.randn(1)
 
      return (W,b)
def modelD(X,W,b): 
    Z=X.dot(W)+b
    A=1/( 1 + np.exp(-Z))
    return A
  
def model (X,W,b):
      Z= X.dot(W)+b  #(n,1)
      A=1+ np.exp(-Z)
      A=1/A         #(n,1)
      return A
def log_loss(A,y):
      e=1e-15
      A=A.T          #(1,n)
      La= np.log(A+e).dot(y)   #(1,1)
      Lb= np.log(1-A+e).dot(1-y)  #(1,1)
      L=La+Lb
      L=-1/len(y)*L
      return L
def log_loss2(A,y):
  
    return 1/len(y)* np.sum(-y * np.log(A) - (1 - y) * np.log(1-A) )
      
def gradient (A,X,y):
    X=X.T
    dW=1/len(y)*(X.dot(A-y))
    db=1/len(y)*np.sum(A-y)
    
    return (dW,db)
def gradients(A,X,y):
    dW= 1/len(y)*np.dot(X.T,(A-y))
    db= 1/len(y) * np.sum(A-y)
    return(dW,db) 

def update(dW,db,W,b,learning_rate):  
    W= W- (learning_rate*dW)
    b= b- (learning_rate*db)
    return (W,b)

def predict(X,W,b):
    Model= model (X,W,b)
    return  Model >= 0.5
        

def main(X,y,I,p,n=10000):
    print(X.shape)
    loss=[]
    loss_T=[]
    acc=[]
    acc_T=[]
              
    #initialiser
    W,b =initialiser(X)
    for i in tqdm(range(n)) :
         A=model (X,W,b)
         D=model(I, W, b)
         if i %10 == 0 :
            L=log_loss(A,y)
            L=L[0,0]
            K=log_loss(D,p)
            K=K[0,0]
          
            #print(L)
            loss.append(L)
            loss_T.append(K)
           
            dW,db= gradients (A,X,y)
            learning_rate=0.01 
            W,b=update(dW, db, W, b, learning_rate)
            y_pred=  predict(X,W,b)
            y_predt=  predict(I,W,b)
            acc.append(accuracy_score(y,y_pred))
            acc_T.append(accuracy_score(p,y_predt))
    #print(loss) 
    #print(acc
    plt.figure(figsize=(12,4)) 
    plt.subplot(1,2,1)      
    plt.plot(loss,label="loss train ") 
    plt.plot(loss_T,label="loss test") 
    plt.subplot(1,2,2)
    plt.plot(acc,label="acc train") 
    plt.plot(acc_T,label="acc test") 
   
    plt.show()   
    return (W,b)     
def front(X,W,b):
    new=np.array([1,6])
    x = np.linspace(-2, 4,100)   
    z=1/W[1]*(-W[0]*x-b)
    plt.scatter(X[:,0],X[:,1],c=y,cmap='summer')
    plt.scatter(new[0],new[1],c='r')
    plt.plot(x,z,c='orange',lw=3)
    
    plt.show()          
     
  