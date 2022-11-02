# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 09:42:33 2022

@author: kemal
"""
# Pandas

import pandas as pd

dictionary = {"Name":["Kemal","Geylani","Yuki","Ali","Veli","Deli"],
              "Age":[15,16,17,33,45,66],
              "Maas":[100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)

head = dataFrame1.head()  # ilk 5 satır önizleme
tail = dataFrame1.tail()  # son 5 satır önizleme

#%%

# Pandas basic methods

print(dataFrame1.columns)

print(dataFrame1.info())

print(dataFrame1.dtypes)

print(dataFrame1.describe()) # numeric feature


#%%

# Indexing and Slicing

print(dataFrame1["Age"])
print(dataFrame1.Age)

dataFrame1["NewFeature"] = [-1,-2,-3,-4,-5,-6] # Yeni özeelik ekleme

print(dataFrame1.loc[:,"Age"]) # Tüm satırlar & Age sütunu 

print(dataFrame1.loc[:3,"Age"]) # Sıfırdan 3. indexe 3 dahil satırlar & Age sütunu

print(dataFrame1.loc[:3,"Name":"Age"])  # Sıfırdan 3. indexe 3 dahil satırlar & Name sütunundan Age sütununa

print(dataFrame1.loc[:3,"Name":"Maas"]) # Sıfırdan 3. indexe 3 dahil satırlar & Name sütunundan Maas sütununa

print(dataFrame1.loc[:3,["Name","Maas"]]) # Sıfırdan 3. indexe 3 dahil satırlar & Name sütunu ve Maas sütunu

print(dataFrame1.loc[::-1,:]) # Tersini al

print(dataFrame1.loc[:,:"Maas"]) # Tüm satırlar & Tüm sütunlar Maas a kadar

print(dataFrame1.loc[:,"NewFeature"]) # Tüm satırlar & NewFeature sütunu 

print(dataFrame1.iloc[:,2]) # Tüm satırlar & 3. sütun

#%%

# Filtering

filtre1 = dataFrame1.Maas > 200 # Maaşı 200 den büyük olanlar
filtre2 = dataFrame1.Age < 20


filtrelenmisData1 = dataFrame1[filtre1]
filtrelenmisData2 = dataFrame1[filtre2]
filtrelenmisData = dataFrame1[filtre1 & filtre2]


#%%

# List and Comprehension

ortMaas = dataFrame1.Maas.mean() # Maasın ortalamasını al

import numpy as np

ortMaasNp = np.mean(dataFrame1.Maas) # Numpy ile ortalama bulmak


dataFrame1["MaasSeviyesi"] = ["Low" if ortMaas > each else "High" for each in dataFrame1.Maas] 

dataFrame1.columns = [each.lower() for each in dataFrame1.columns] # her sütun ismini küçük harf yap



#%% drop and concatenating

dataFrame1.drop(["newfeature"], axis = 1, inplace = True) # newfeature sütunu kaldır.

data1 = dataFrame1.head()
data2 = dataFrame1.tail()

# Vertical birlestir

dataConcatV = pd.concat([data1,data2], axis = 0)

# Horizontal birlestir

maas = dataFrame1.maas
age = dataFrame1.age

dataConcatH = pd.concat([maas,age], axis = 1)


#%% Transforming data

dataFrame1["NewList"] = [each*2 for each in dataFrame1.age] #  Yaşların 2 katını yeni sütuna yaz

# Apply()

def multiply(age):
    return age*2

dataFrame1["ApplyMetoduNewList"] = dataFrame1.age.apply(multiply) #  Yaşların 2 katını yeni sütuna yaz (Apply metodu ile)




