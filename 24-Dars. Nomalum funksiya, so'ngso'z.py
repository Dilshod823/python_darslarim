# 24-Dars. so'ngso'z (Nomsiz funksiya)

# "lambda" funksiyasi

import math 
uzunlik = lambda pi, r : 2*pi*r
#print(uzunlik(math.pi,10))

product = lambda x, y: x ** y
#print(product(2, 3))

def daraja(n):
    return lambda x: x**n

kvadrat = daraja(2)
print(kvadrat(3))
kub = daraja(3)
print(kub(3))
print(f"3 ning kvadrati: {kvadrat(3)} ga,\n"
      f"kubi esa: {kub(3)} ga teng")



# "map" funksiyasi

from math import sqrt

sonlar = list(range(11))
ildizlar = list(map(sqrt, sonlar))
#print(sonlar)
#print(ildizlar)

sonlar = list(range(11))

def daraja2(x):
    """berilgan sonning kvadratini hisoblab qaytaruvchi funksiya"""
    return x*x

#print(list(map(daraja2, sonlar)))


kvadratlar = list(map(lambda x:x*x, sonlar))
#print(kvadratlar)

a = [4, 5, 6]
b = [7, 8, 9]
a_plus_b = list(map(lambda x, y: x+y, a,b))
print(a_plus_b)


# "filter" funksiyasi

import random as r
sonlar = r.sample(range(100),10)

def juftmi(n):
    """x juft bo'lsa True, aks holda False qaytaruvchi funksiya"""
    return n%2==0

juft_sonlar = list(filter(juftmi, sonlar))
#print(sonlar)
#print(juft_sonlar)

import random as r

sonlar = r.sample(range(100),10)
juft_sonlar = list(filter(lambda son: son%2==0, sonlar))

#print(sonlar)
#print(juft_sonlar)

mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

mevalar_b = list(filter(lambda meva: meva.startswith('a'),mevalar))
#print(mevalar_b)

mevalar2 = list(filter(lambda meva: len(meva)<=5, mevalar))
print(mevalar2)