# -*- coding: utf-8 -*-

# Yorum satırı için # kullanılır.

#%%

# Variables (değişkneler)

var1 = 10 #integer
var2 = 5  #int

gun = "pazartesi" #String

var3 = 10.0 #Double or (Float)

#%%

#String

s = "Bu gün pazartesidir."

variable_type = type(s)

print(s)

var1 = "ist"
var2 = "ankara"

print(var1+var2)

uzunluk = len(var2)

print(uzunluk)

#%%

# Numbers

#int

integer_deneme = -50

# double = float

float_deneme = -50.5

#%%

# Built in functions 

str1 = "deneme"

str2 = "1005"

float1 = 10.6

#%%

# User defined functions

var1 = 20
var2 = 50

output = (((var1+var2)*50)/100.0)*(var1/var2)

def myFirstFuction (a,b):
    
    output = (((a+b)*50)/100.0)*(a/b)
    
    return output


def deneme():
    
    print("Hello world!")
    
    
#%%

# defoult & flexible functions

# Defoult

def cemberCevre(r,pi = 3.14):
    
    """
    Çember çevresi hesapla
    
    input (parametre) : r
    
    output : cevre
    
    """
    
    cevre = 2 * pi * r
    
    return cevre 


# Flexible

def heaspla(boy,kilo,*args):
    
    print(args)
    
    output1 = (boy + kilo)*args[0]
    
    return output1

#%%

# Homework

# def x(y):

#     y = y + [2]

#     print(y)

# c = [1,2,3]

# x(c) = ?

# print(len(c)) = ?   

# c = c+3

# 3. soru

def s(x, y = 2):

    c = 2

    for i in range(y):

        c = c + x

    return c

#%%

# Quiz1

yas = 10
name = "kemal"
surname = "yuki"

def functionQuiz(yas, name, *args, ayakkabiNumara = 35):
    
    print("yas : ",yas, "name : ",name, "surname : ",surname, "ayakkabı numarası : ",ayakkabiNumara)
    print(float(yas))
    print(type(name))
    
    output = args[0]*yas
    
    return output

sonuc = functionQuiz(yas, name, surname)

print("Output : ",sonuc)
    





    
    

    


