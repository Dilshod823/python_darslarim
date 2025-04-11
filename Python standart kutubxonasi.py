# Python standart kutubxonasi

import datetime as dt

# datetime
hozir = dt.datetime.now()
print(hozir)

# date
bugun = dt.date.today()
print(f"Bugungi sana: {bugun}")
ertaga = dt.date(2025, 4, 11)
print(f"Ertangi sana: {ertaga}")

# time
hozir = dt.datetime.today()
vaqthozir = hozir.time()
print(f"Hozirgi soat: {vaqthozir}")
vaqtkeyin = dt.time(11, 22, 33)
print(vaqtkeyin)

# Sanalar orasidagi farq

bugun = dt.date.today()
ramazon = dt.date(2026, 2, 21)
farq = ramazon-bugun
print(f"Kyingi ramazongacha {farq.days} kun qoldi")

# Soatlar orasidagi farq
hozir = dt.datetime.now()
fudbol = dt.datetime(2025, 4, 22, 10, 00)
farq = fudbol-hozir
sekundlar = farq.seconds
minutlar = int(sekundlar/60)
soatlar = int(minutlar/60)
print(f"Fudbol boshlanishiga {farq.days} kunu {soatlar} soat qoldi")


# Math moduli

import math

PI = math.pi
print(f"PI ning qiymati: {PI}")
E = math.e
print(f"E ning qiymati: {E}")

# trigonometriya
math.sin(math.pi/2)
math.cos(0)
math.tan(PI)

# radianlar va burchaklar o'rtasida konvertatsiya
print(math.degrees(math.pi/2))
print(math.radians(90))

# # logarifmlar
# natural logarifm
math.log(5)
# 10 asosli logarifm
math.log10(100)

# sonlarni yaxlitlash
x = 4.5
print(math.ceil(x))
print(math.floor(x))

# Kvadrat ildiz
x = 81
math.sqrt(x)

# Darajaga oshirish
math.pow(x, 3)
math.pow(x, 5)
math.pow(x, 1/3)


# pprint moduli

from pprint import pprint
import json

filename = 'bemor.json'
with open(filename) as f:
    bemor = json.load(f)

pprint(bemor)

import requests
r = requests.get('https://api.github.com')

# pprint(r.json())


# Regex (Regular Expression)
import re

word1 = "темир"
word2 = "томир"
word3 = "тулпор"

andoza = "^т...р"

print(re.match(andoza, word1))
print(re.match(andoza, word2))
print(re.match(andoza, word3))

andoza = "^т...р"
matches = []
#for word in words:
#    if re.match(andoza, word):
#        matches.append(word)
        
print(matches)


# Emailni ajratib olish

matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """

andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
email = re.findall(andoza,matn)
print(email)



# Kuchli parolni tekshirish
# Quyidagi andoza ham ihateregex.io sahifasidan olindi
andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
msg = "Yangi parol kiriting"
msg += '(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, '
msg += '1 ta son va 1 ta maxsus belgi boʻlishi kerak): '

while True:
    password = input(msg)
    if re.match(andoza,password):
        print("Maxfiy so'z qabul qilindi")
        break
    else:
        print("Maxfiy so'z talabga javob bermadi")

