# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 11-Dars. Bir nachta shartlarni ko'rish

# Amaliyot
#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

son = float(input("Bironta juft son kiriting>>>"))
if son%2:
    print("Bu juft son emas")
else:
    print("Rahmat!")
    
    # Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:

    yosh = int(input("Yoshingiz nechida?\n>>>"))
    if yosh<4 or yosh>60:
        narh = 0
    elif yosh<18:
        narh = 10000
    else:
        narh = 20000
    print(f"Sizga kirish {narh} so'm")
    
# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring

print("Iltimos ikkita son kiriting")
x = float(input("Birinchi sonni kiriting:>>>"))
y = float(input("Ikkinchi sonni kiriting:>>>"))
if x==y:
    print("x==y")
elif x<y:
    print("x<y")
else:
    print("x>y")
    
# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. 
# Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang.
# Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

mahsulotlar = ['tarvuz', 'qovun', 'kartoshka', 'piyoz', 'sabzi', 'lomon', 'olma', 'anor', 'apelsin', 'suv']
savat = []
for n in range(5):
    savat.append(input(f"{n+1}-mahsulotni kiriting:>>>"))
    
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor")
    else:
        print(f"Do'konimizda {mahsulot} yuq")