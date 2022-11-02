# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 19:12:42 2022

@author: kemal
"""

# OOP

class calisan:
    
    zamOran = 1.8
    counter = 0
    
    def __init__(self,isim,soyisim,maas): # Constructor
        
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim+soyisim+"@yukisoft.com"
        calisan.counter = calisan.counter + 1
        
    def giveNameSurname(self):
        
        return self.isim + " " + self.soyisim
    
    def zamYap(self):
        
        self.maas = self.maas + (self.maas)*(self.zamOran)
    
    
# isci1 = calisan("Kemal", "YUKİ", 7000)
# print(isci1.giveNameSurname)
# print(isci1.maas)
# print(isci1.email)
        
calisan1 = calisan("Kemal", "YUKİ", 7000)   
# print(calisan1.maas)
# calisan1.zamYap()
# print("yeni maas : ", calisan1.maas)

calisan2 = calisan("Kem", "Y", 700)  
calisan3 = calisan("Kem3", "Y3", 800) 
calisan4 = calisan("Kem4", "Y4", 7900) 
calisan5 = calisan("Kem5", "Y5", 900) 

liste = [calisan1,calisan2,calisan3,calisan4,calisan5]

maxMaas = -1
index = -1

for each in liste:
    if (each.maas > maxMaas):
        maxMaas = each.maas
        index = each

#%%

# Sınav 6

class A:

    global a

    a = 5

    def __init__(self,x = 4):

        self.x = x

    def sum(self):

        return a + self.x

x = A(5)

x.sum()

str1 = "sshgs"




















        

        
