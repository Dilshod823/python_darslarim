# 18-Dars. While sikli

# 1-Savol.

# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

buyurtmalar = []
while True:
    savol = input("buyurtmangizni kiriting:")
    savol += ("Buyurtmani tugatganingizdan so'ng 'stop' deb yozing") 
    buyurtmalar.append(savol)
    javob = input("Yana buyurtma kiritasizmi? (ha/yo'q)")
    if javob == "yo'q":
        
        break
    else:
        continue
    
print(buyurtmalar)


# 2-Savol.

# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. 
# Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.

mahsulotlar = {}
while True:
    mahsulot = input("Mahsulot nomini kiriting:")
    narh = input(f"{mahsulot}ning narhini kiriting:")
    mahsulotlar[mahsulot]=float(narh)
    javob = input("Yana mahsulot kiritishni xoxlaysizmi? (ha/yo'q)")
    if javob == "yo'q":
        break
    else:
        continue
print(f"{mahsulot}ning narhi {narh}")


# 3-savol.

# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan-
# solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.

buyurtmalar = ['olma', 'anor', 'sabzi', 'uzum']
mahsulotlar = {'olma':12000,
             'anor':15000,
             'limon':10000,
             'apelsin':18000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()}-{narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")