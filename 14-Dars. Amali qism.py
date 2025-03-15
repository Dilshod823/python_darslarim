# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 15:14:51 2025

@author: HP
"""

# 15-dars. Dictionary(amaliy qismi)

# 1-savol

# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. 
# Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, 
# alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 
Python_lugat = {
    'print':'dasturni konsolga chiqaradi',
    'string':'matn',
    'integer':'butun son',
    'float':'onlik son',
    'type':"o'zgaruvchida saqlangan malumot turini tekshiradi",
    'input':'foydalanuvchidan biron nima sorashda ishlatiladi',
    'list':"ro'yhat",
    'append':"ro'yhatga element qo'shadi",
    'insert':"ro'yhatga element qo'shadi",
    'del':"ro'yxatdan elementni o'chiradi",
    'remove':"ro'yxatdan elementni o'chiradi",
    'pop':"ro'yxatdan elementni sug'urib olishda ishlatiladi",
    'sort':"ro'yxatni alifbo ketma-ketligida chiqaradi",
    'sort(reverse True)':"ro'yxatni alifboga qarshi chiqaradi",
    'sorted':"ro'yxatni alifbo ketma-ketligida chiqaradi",
    'reverse':"ro'yxatni alifboga qarshi chiqaradi",
    'range':'malum oraliqdagi sonlar ketma-ketligini yaratamiz',
    'min':'sonlardan tashkil topgan royxatdagi sonlarni eng kichigini konsolga chiqarishda foydalanamiz',
    'max':'sonlardan tashkil topgan royxatdagi sonlarni eng kattasini konsolga chiqarishda foydalanamiz', 
    'sum':'sonlardan tashkil topgan royxatdagi sonlarni ortasini hisoblab konsolga chiqarishda foydalanamiz',
    'tuple':"o'zgaruvchan ro'yxatni o'zgarmas ro'yxatga o'tqazadi"
    }
Python_lugat['if'] = 'bir nechta shartlarni bajarishda qollaniladi'
Python_lugat['else'] = 'bir nechta shartlarni bajarishda qollaniladi'
for key, value in sorted(Python_lugat.items()):
    print(f"{key.title()} - {value}")
    
    
# 2-savol


# Davlatlar va ularning poytaxtlari lug'atini tuzing. 
# Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, 
# alifbo ketma-ketligida konsolga chiqaring. 

davlatlar = {
    "O'zbekiston": "Toshkent",
    "Qozog'iston": "Astana",
    "Qirg'iziston": "Bishkek",
    "Tojikiston": "Dushanbe",
    "Turkmaniston": "Ashxobod"
}
print("O'rta osiya davlatlari;")
for davlat in sorted(davlatlar.keys()):
    print(davlat.upper())
    
print('\nDavlatlarning poytaxtlari:')
for poytaxt in davlatlar.values():
    print(poytaxt.title())
    
    
# 3-Savol


# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring.
# Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

davlatlar = {
    "O'zbekiston": "Toshkent",
    "Qozog'iston": "Astana",
    "Qirg'iziston": "Bishkek",
    "Tojikiston": "Dushanbe",
    "Turkmaniston": "Ashxobod"
}
#print("O'rta osiya davlatlari;")
#for davlat in sorted(davlatlar.keys()):
   # print(davlat.upper())
    
#print('\nDavlatlarning poytaxtlari:')
#for poytaxt in davlatlar.values():
 # print(poytaxt.title())
 
davlat = input("Qaysi davlatni poytaxtini bilishni xoxlaysiz:").lower()
if davlat in davlatlar:
    print(davlat)
