# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 22:05:33 2022

@author: kemal
"""

# list

#%%

liste = [1,2,3,4,5,6]

type(liste)

listeString = ["ptesi", "salı", "çarş"]

type(listeString)

value = liste[-1]

print(value)

liste.append(7)

liste.remove(1)

#%%

# Tuple

t = (1,2,3,3,3,4,5,6)

t.count(3)
t.index(3)

#%%

# Dictionary

dictionary = {"ali":32, "veli":45, "ayşe":13}

# ali, veli, ayşe = keys
# 32,45,13 = values

def deneme():
    
    dictionary = {"ali":32, "veli":45, "ayşe":13}
    
    return dictionary

d = deneme()

#%%

# sınav 4

a = "sakin calismaktan vazgecmeyin"

a[1]+a[0]+a[8]+a[1] + " " + a[-11:] = ?

#%%

# Conditionals

var1 = 20
var2 = 20


if(var1 > var2):
    
    print("var1 büyüktür var2")
    
elif(var1 == var2):
    
    print("var1 ve var2 eşitler")
        
else:
    
    print("var1 küçüktür var2")
    

liste = [1,2,3,4,5,6,7,8,9]

if 7 in liste:
    
    print("evet")
    
else:
    
    print("hayır")
    

#%%

# Quiz

# Inputs = years
# Outputs = yüzyıl
# 1 < years < 2005



def sunuc(year):

    stringYear = str(year)

    if (len(stringYear)<3):          # 0 <= 99
        return 1

    elif (len(stringYear) == 3):     # 100 200 300 .... 900   
        if (stringYear[1:3] == "00"):
            return int(stringYear[0])
        else: 
            return int(stringYear[0])+1 # 101 450 862 ....

    else:
        if (stringYear[2:4] == "00"): # 1000 2000 .... 2005
            return int(stringYear[:2])
        else:
            return int(stringYear[:2])+1
    
#%%

# Loops

for each in range(1,11):
    print(each)
    
for each in "Ankara İstanbul DİYARBAKIR":
    print(each)
    
for each in "İstanbul DİYARBAKIR".split():
    print(each)
    
liste = [1,2,3,4,5,6,7,8,9,10]

count = 0

for each in liste:
    count = count + each
    print(count)
    

# While

i = 0

while(i < 5):
    print(i)
    i = i + 1
    
sinir = len(liste)
each = 0
count = 0

while(each < sinir):
    count = count + liste[each]
    each = each + 1

#%%

liste = [1,2,3,4,5,6,4,23,67,21,-500,23,451,67]

mini = 1000000

for i in liste:
    
    if (i < mini):
        mini = i
        
    else:
        continue
    


print(mini)

#%%
    

        
























        

 




