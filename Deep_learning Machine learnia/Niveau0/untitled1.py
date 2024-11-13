

import numpy as np
import matplotlib.pyplot as plt 

  
from utilities import *


X_train, y_train, X_test, y_test = load_data()
print(X_train.shape)
print(y_train.shape)
print(np.unique(y_train, return_counts=True))

print(X_test.shape)
print(y_test.shape)
print(np.unique(y_test, return_counts=True))



plt.figure(figsize=(16, 8))
for i in range(1, 11):
    plt.subplot(4, 5, i)
    plt.imshow(X_train[i], cmap='gray')
    plt.title(y_train[i])
    plt.tight_layout()
plt.show()


X_train_reshape =X_train.reshape(X_train.shape[0],-1)/X_train.max()
X_test_reshape =X_test.reshape(X_test.shape[0],-1)/X_train.max()

print(X_train_reshape.shape)
print(X_test_reshape.shape)