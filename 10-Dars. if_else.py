# 10-Dars. if-else


# if operatori

avtolar = ['audi','bmw','volvo','kia','hyundai']
for avto in avtolar:
    if avto == 'bmw':
         print(avto.upper())
    else:
         print(avto.title())
         
# TRUE/FALSE
ism = 'Ali'

# matnlarni solishtirish
ism = 'Ali'
ism.lower() =='ali'

# Qiymatlarning teng emasligini tekshirish
ism = input('Ismingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
    print(f"Uzr, {ism.title()} biz Alini kutayapmiz.") # quyidagi xabar chiqadi
else:
    print("Salom, Ali")
    
# Sonlarni solishtirish
yosh = int(input("Yoshingiz nechida?>>>"))
if yosh>=18: # yosh 18 dan katta yoki teng bo'lsa
    print('Xush kelibsiz!')
else: # ask holda
    print('Kirish mumkin emas!')
    
    
yosh = int(input("Yoshingiz nechida?>>>"))
if yosh>=18:
    print("Xush kelibsiz!")
else:
    print("Sizga kirish mumkin emas")
    
    
login = input("Yangi login tanlang:")
if len(login)<=5:
    print("Login 5 harfdan ko'proq bo'lishi kerak")
    
    
# sonlarni solishtirishda arifmetik ifodalar yozish
yil = int(input("Tug'ilgan yilingizni kiriting:"))
if 2025-yil<18:
    print(f"Yoshingiz {2025-yil} yoshda ekan")
    print("Kirish mumkin emas")
else:
    print("Xush kelibsiz!")
    

# Bir qator if/else
yosh = int(input("Yoshingiz nechida>>>"))
if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")


#  AMALIYOT

# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing,-
# ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())
        
# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
     if car != 'gm':
        print(car.upper())
     else:
        print(car.title())
        
# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" 
# xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.

login = input("Logininginingzini kiriting:>>>").title()
if login == 'Admin':
    print("Xush kelibsiz, Admin. Foydalanuvchi ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {login}!")
    
# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga- 
# teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.

print("2 ta son kiriting")
b_son = float(input("Birinchi sonni kiriting :"))
ik_son = float(input("Ikkinchi sonni kiritning :"))
if b_son == ik_son:
    print("Sonlar teng")

# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", -
# agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 

son = float(input("Iltimos biror son kiriting:"))
if son<0:
    print("Manfiy son")
else:
    print("Musbat son")
    
# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. -
# Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 

son = float(input("Iltimos biron son kiriting:"))
if son>0:
    print(son**(1/2))
else:
    print("Musbat son kiriting")