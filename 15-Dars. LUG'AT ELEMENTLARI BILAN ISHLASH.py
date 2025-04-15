# 15-Dars. LUG'AT ELEMENTLARI BILAN ISHLASH


# .items metodi
talaba_0 = {
    'ism':'alijon',
    'familiya':'shamshiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
    }

print(talaba_0.items())
    
# For silki bilan .items metodi
for kalit, qiymat in talaba_0.items():
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat} \n")
    
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }

for k, q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")
    
# .keys metodi
mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }

print(mahsulotlar.keys())

# .values() metodi
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }

print(telefonlar.values())
print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
    print(tel)
    
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

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
    print(tel)
    
print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in set(telefonlar.values()):
    print(tel)

print('Do\'kondagi mahsulotlar:')
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

bozorlik = ['anor','uzum','non','baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Iltimos, do'koningizga {buyum} ham olib keling")
        
print("Do'konimizdagi mahsulotlar:")    
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())        
        
        
        
# AMALIYOT

# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni-
# for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 
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

print("Quyida Python dasturlash tiliga oid terminlar va ularning vazifalari")
for kalit, qiymat in sorted(Python_lugat.items()):
    print(f"{kalit}-{qiymat}")
    
# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni-
# alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 
capital = {
    "o'zbekiston": 'Toshkent',
    "qozog'iston": 'Nursulton',
    "tojikiston": 'Dushanbe',
    "turkmaniston": 'Ashxobod'
}
print("Quyida O'rta Osiyo davlatlari:")
for davlat in sorted(capital.keys()):
    print(davlat.title())
    
print("Quyida O'rta Osiya davlatlarining poytaxtlari:")
for p in sorted(capital.values()):
    print(p.title())

# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. Agar foydalanuvchi -
# lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
davlat = input("Qaysi davlatning poytaxtini bilishni xohlaysiz?: ").lower()

if davlat in capital:
    print(f"{davlat.title()}ning poytaxti: {capital[davlat]}")
else:
    print("Bizda bunday ma'lumot yo'q")

# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang.
# Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q"
# degan xabarni chiqaring.
# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang.
# Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q"
# degan xabarni chiqaring.
menu = {
    'osh': 30000,
    'manti': 5000,
    "lag'mon": 25000,
    'tabaka': 20000,
    'shashlik': 15000,
    'norin': 18000,
    'kabob': 22000,
    'somsa': 4000,
    'chuchvara': 12000,
    'beshbarmak': 27000
}

buyurtmalar = []
print("3 ta taom buyurtma bering:")

for i in range(3):
    taom = input(f"{i+1}-taom: ").lower()
    buyurtmalar.append(taom)

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} — {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q")
        
        
        
        