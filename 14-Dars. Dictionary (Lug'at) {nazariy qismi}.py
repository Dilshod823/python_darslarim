# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 14:39:10 2025

@author: HP
"""

# 15-Dars. Lug'at bilan ishlaymiz
talaba_0 = {
    'ism':'ali ',
    'familiya':'xudoyqulov',
    'yosh':24,
    'kurs':4
    }
print(talaba_0.items())

talaba_0 = {
    'ism':'ali ',
    'familiya':'xudoyqulov',
    'yosh':24,
    'kurs':4
    }
for key, value in talaba_0.items():
    print(f"Kalit: {key}")
    print(f"Qiymat: {value}")
  
    
telefonlar = {
    'ali':'samsung',
    'vali':'nokia',
    'hasan':'galaxy',
    'husan':'redmi'
    }
for k, q in telefonlar.items():
    print(f"{k.title()} ning telefoni {q}")
    
    
# .keys metodi
mahsulotlar = {
    'olma':10000,
    'anor':12000,
    'sabzi':5000,
    'uzum':20000
    }
print(mahsulotlar.keys())


mahsulotlar = {
    'olma':10000,
    'anor':12000,
    'sabzi':5000,
    'uzum':20000
    }
print("Do'kondagi mahsulotlar:")
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())
    
print("Do'kondagi mahsulotlar:")
for mahsulot in mahsulotlar:
    print(mahsulot.title())
    
    
bozorlik = ['olma', 'anor', 'bexi', 'shaftoli']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]}so'm")
        
        
for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Ilyimos, do'koningizga {buyum} ham olib keling ")
        
        
print("Do'konimizdagi mahsulotlar:")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())
    
    
# .values
print(telefonlar.values())

print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
for tel in telefonlar.values():
    print(tel)
    
    
# # set funksiyasi
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }
print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
for tel in set(telefonlar.values()):
    print(tel)
    
    
# sets (ma'lumot turi)
toys = {'bear', 'bullsh', 'car', 'bear', 'ari'}
print(toys)
