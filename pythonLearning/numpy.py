# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 17:29:29 2022

@author: kemal
"""

# Numpy

import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

print(array.shape)

a = array.reshape(3,5)

print("Shape : ", a.shape)

print("Dimension : ", a.ndim)

print("Data Type : ", a.dtype.name)

print("Size : ", a.size)

print("Type : ", type(a))

arrayNew = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,1]]) # Reshape kullanmadan 3*4 matris

zeros = np.zeros((3,4))

zeros[0,0] = 5 # 1. satır 1. sütun elemanı 5 yap

np.ones((3,4))

np.empty((3,4))

a = np.arange(10,50,5)

a = np.linspace((10,50,20))

a = np.linspace(10,50,20)

#%%

# Numpy Operations 

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)

print(a-b)

print(a**2)

print(np.sin(a))

print(a < 2)

a = np.array([[1,2,3],[4,5,6]]) 
b = np.array([[1,2,3],[4,5,6]])

# Element Wise Product

print(a*b)

a.dot(b.T)

print(np.exp(a))

a = np.random.random((5,5))

print(a.sum())
print(a.max())
print(a.min())

print(a.sum(axis = 0))
print(a.sum(axis = 1))

print(np.sqrt(a))
print(np.square(a))

print(np.add(a,a))

a = np.array([[1,2,3],[4,5,6]])

b = np.array([[1,2,3],[4,5,6]])

a.dot(b.T)

#%% 

# Indexing and Slicing

import numpy as np

array = np.array([1,2,3,4,5,6,7])

print(array[0])

print(array[0:4]) # 0 dan 4 e kadar al. 4. dahil değil.

reverseArray  = array[::-1] # matrisin tersini alır.

array1 = np.array([[1,2,3,4,5],[6,7,8,9,10,]])

print(array1[1,1]) # 2. satır 2. sütun

print(array1[:,1]) # 2. sütun

print(array1[1,1:4]) # 2. satır. 2-3-4 sütunlar

print(array1[-1,:]) # son satır. Tüm sütunlar.

print(array1[:,-1]) # tüm satırlar. son sütun.


#%%

# Shape manipultion

array = np.array([[1,2,3,],[4,5,6],[7,8,9]])

a = array.ravel() # tek satır yapmak için.

array2 = a.reshape(3,3)

arrayTr = array.T


#%%

# Stacking Array - Array birleştirme

array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])

arrayVertical = np.vstack((array1,array2))    # Dikey birleştir.
arrayHorizontal = np.hstack((array1,array2))  # Yatay birleştir.


#%%

# Convert and Copy

liste = [1,2,3,4]

array = np.array([1,2,3,4])

listeConvert = list(array) # Array (matris) i listeye çevirme.

arrayConvert = np.array(liste) # Listeyi Array çevirme.

# ---------------------------------------------------------

a = np.array([1,2,3])

b = a
c = a


 






























 

  




































































































