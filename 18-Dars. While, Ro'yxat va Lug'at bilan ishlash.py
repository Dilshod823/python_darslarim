# 18-Dars. While, Ro'yxatlar va Lug'atlar.


# While yordamida ro'yxatni to'ldirish
ismlar = []

print("Yaqin do'stlaringiz ro'yxatini tuzamiz")
n=1 # ismlarni sanash uchun o'zgaruvchi
while True:
    savol = f"{n}-do'stingizni ismini kiriting :"  
    ism = input(savol)
    ismlar.append(ism)
    javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
    n += 1
    if javob != 'ha':
        break
    
print("Do'stlaringiz ro'yxati:")
for ism in ismlar:
    print(ism.title())
    
    
# While yordamida lug'atni to'ldiramiz
print("Do'stlaringiz yoshini saqlaymiz")

dostlar = {}
ishora = True
while ishora:
    ism = input("Do'stingiz ismini kiriting :")
    yosh = input(f"{ism.title()}ning yoshini kiriting :")
    dostlar[ism] = int(yosh)
    
    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
    if javob == "yo'q":
        break
    
for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")
    
    
# While yordamida ro'yxat elementlarini o'chirish
cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
    cars.remove('nexia') # nexia ni ro'yxatdan olib tashla
print(cars)


# Ro'yxatdan ro'yxatga element ko'chirish
talabalar = ['hasan', 'husan', 'botir', 'ali']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting :")
    print(f"{talaba.title()}ning bahosi qo'yildi")
    baholangan_talabalar[talaba] = int(baho)



# AMALIYOT
# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
buyurtmalar = []
while True:
    buyurtma = input("Buyurtmangizni kiriting :")   
    buyurtmalar.append(buyurtma)
    takrorlash = input("Yana buyurtma qo'ashaszimi? (ha/yo'q)").lower()
    if takrorlash == "yo'q":
        break
    
print(buyurtmalar)


# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing.-
# Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
mahsulotlar_narhlari = {}
while True:
    mahsulot = input("Mahsulot nomini kiriting :")
    narh = input(f"{mahsulot}ning narhini kiriting :")
    mahsulotlar_narhlari[mahsulot] = float(narh)
    takror = input("Yana mahsulot qo'shasizmi? (ha/yo'q)")
    if takror == "yo'q":
        break
    
for mahsulot, narh in mahsulotlar_narhlari.items():
    print(f"{mahsulot}ning narhi: {narh}")
    
# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan-
# solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
buyurtmalar = []
buyurtmalar_narhlari = {}
while True:
    buyurtma = input("Buyurtmangizni kiriting :")
    narh = input(f"{buyurtma}ning narhini kiriting :")
    buyurtmalar_narhlari[buyurtmalar] = int(narh)
    takror = input("Yana buyurtma qo'shasizmi? (ha/yo'q)")
    if takror == "yo'q":
        break
    
    for buyurtma, narh in buyurtmalar.values():
        if buyurtma in buyurtmalar_narhlari:
            print(f"{buyurtma}ning narhi: {narh}")
        else:
             print("Bizda bu mahsulot yo'q")




