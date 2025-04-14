# 6-Dars. SONLAR

# Integer - Butun sonlar
a = 20 # Sonlar musbat yoki
b = -30 # manfiy bo'lishi mumkin
c = a + b
print(c) 

# Kvadratning yuzini hisoblaymiz
kvdrt_tmni = 20 # Kavdratning tomoni 20 ga teng
kvdrt_yuzi = kvdrt_tmni**2 # Kvadrat yuzini hisoblaymiz
print(kvdrt_yuzi)

# Float - O'nlik son
pi = 3.14159 # o'nlik son (float)
radius = 10  # butun son (integer)
diametr = 2*radius
print("Aylana uzunligi ", pi*diametr, " ga teng.")

# Butun sondan o'nlik songa
a = -20
b = 40
c = b/a
print(c) # natija o'nlik son bo'ladi

a = 2
b = 3.0
# Quyidagi arifmetik amallarning natijasi o'nlik son hosil qiladi
print(a+b) 
print(a*b)
print(a**b)
print(2*(a+b))

# Uzun sonlarni kiritish
aholi_soni = 7_594_000_000 # o'zmizga qulay bo'lishi uchun shinday yozdik
print("Yer kurrasida", aholi_soni, "ga yaqin odam yashaydi")

# Konstanta
PI = 3.14159
raduis = 21.2

# Bir nechta o'zgaruvchiga qiymat berish
a, b, c = 10, -7.25, 30

# O'zgaruvchi turini almashtirish
ism = 'Jobir'
yosh = 36
xabar = ism + ' ' + str(yosh) + 'yoshda'
print(xabar)

# Pythonda bir turdagi o'zgaruvchini boshqa turdagi o'zgaruvchiga o'tqazish (typecasting)

# str() - int yoki float turidagi sonlarni matnga o'zgartiradi
# float() - matn yoki int ko'rinishidagi qiymatlarni o'nlik songa o'zgartiradi
# int() - matn yoki float ko'rinishidagi qiymatlarni butun songa o'zgartiradi. Bunda matn butun son ko'rinishida bo'lishi kerak.
ism = 'Jobir'
yosh = 36
xabar = ism + ' ' + str(yosh) + ' yoshda'
print(xabar)

# O'zgaruvchi turini tekshirish
# o'zgaruvchi turini tekshirishda "type()" funksiyasidan foydalanamiz
ism = 'Jobir'
yosh = 36
print(type(ism))  # ism degan o'zgaruvchining turini konsolga chiqaramiz
print(type(yosh)) # ismyosh degan o'zgaruvchining turini konsolga chiqaramiz


# INPUT() VA SONLAR
#1 foydalanuvchining tug'ilgan yilini so'raymiz
t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
#2 foydalanuvchi yoshini xisoblaymiz
yosh = 2020 - t_yil # 
#3 foydalanuvchi yoshini konsolga chiqaramiz
print("Siz " + str(yosh) + " yoshda ekansiz")


# AMALIYOT
# Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
son = float(input("Istalgan son kiriting:\n>>>"))
print(f"{son} ning kvadrati: {son**2} ga "
      f"kubi esa: {son**3} ga teng")


# Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur
yosh = int(input("Yoshingiz nechida?\n>>>"))
tyil = 2025-yosh
print(tyil)

# Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning
# yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur
print("Ikkita son kiriting")
b_son = float(input("Birinchi sonni kiriting:"))
ik_son = float(input("Ikkinchi sonni kiriting:"))
print(f"{b_son} va {ik_son} yig'indisi: {b_son+ik_son} ga,\n  ayirmasi: {b_son-ik_son} ga, ko'paytmasi: {b_son*ik_son} ga, bo'linmasi esa: {b_son/ik_son} ga teng")