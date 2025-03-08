# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 01:12:26 2025

@author: HP
"""

yosh = int(input("Yoshingzi nechida?\n>>>"))
if yosh<=4:
    narh = 0
elif yosh<18:
    narh = 5000
elif yosh<64:
    narh = 8000
else:
    narh = 10000
print(f"Sizga kirish {narh} so'm")    


kun = input("Bugun qaysi kun?\n>>>")
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print("Bugun dam olish kuni")
else:
    print("Bugun ish kuni")
    
    
kun = input("Bugun qaysi kun?")
harorat = float(input("Havo harorati qanday?"))

if kun.lower()=='yakshanba' and harorat>=30:
    print("Cho'milgani ketdik!")
elif kun.lower()=='yakshanba' and harorat<30:
    print("Uyda utiramiz")
    
    
kun = input("Bugun qaysi kun?")
harorat = float(input("Havo harorati qanday?"))

if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
    print("cho'milgani ketdik")
elif (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat<30:
    print("uyda dam olamiz")
    
    
ovqat = 15000
choy = True
salat = True

if choy and salat:
    ovqat = ovqat + 10000
elif choy or salat:
    ovqat = ovqat + 5000
print(f"Jami {ovqat}") 


menu = ['osh', 'manti', 'somsa', 'shashlik', 'tabaka']
ovqat = input("Siz nima ovqat yeysiz?>>")

if ovqat in menu:
    print("Buyurtma qabul qilindi")
else:
    print("Afsuski bizda bunday ovqat yuq")
    
    
menu = ['osh', 'manti', 'somsa', 'shashlik', 'tabaka']
ovqat = input("Siz nima ovqat yeysiz?>>")

if ovqat not in menu:
    print("Afsuski bizda bunday ovqat yuq")
else:
    print("Buyurtma qabul qilindi")
    
    
menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]

for taom in buyurtmalar:
    if taom in menu:
        print(f"Menuda {taom} bor")
    else:
        print(f"Kechirasiz, menuda {taom} yuq")
        
        
menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = []
for taom in range(3):
    buyurtmalar.append(input(f"{taom+1}-taomni kiriting:\n>>>"))
 
if buyurtmalar:    
    for taom in buyurtmalar:
      if taom in menu:
        print("Buyurtma qabul qilindi")
      else:
        print(f"Afsuski, menuda {taom} yuq")