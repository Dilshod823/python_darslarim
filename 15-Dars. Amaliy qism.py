
# 15-Dras. Dictionary \ Amaliyot

# 1-savol.

# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing.-
# Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 

python_izohli_lugat = {
    'Boolean':'Mantiqy qiymat',
    'float':"o'nlik son",
    'integer':'butun  son',
    'for':'biror shartni qayta-qayta bajarish tsikli',
    'if':'shartlarni tekshirish operatori',
    'print':'biron kodni konsolga chiqaradi',
    'type':"o'zgaruvchini tarkibini tekshiradi",
    'tuple':"o'zgarmas ro'yxat",
    'else':'shartlarni tekshirish operatori',
    'elif':'shartlarni tekshirish operatori'
    }
for key, value in sorted(python_izohli_lugat.items()):
    print(f"{key} - {value}")
    

# 2-savol.

# Davlatlar va ularning poytaxtlari lug'atini tuzing.-    
# Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida-
# alifbo ketma-ketligida konsolga chiqaring. 

davlatlar_poytaxtlar ={
    'aqsh':'washington',
    'italiya':'rim',
    'malayziya':'kaula-lumpur',
    "o'zbekiston":"toshkent",
    "qirg'iziston":"nursulton",
    "qozog'iston":"bishkek",
    'rossiya':'moskva',
    "singapur":'singapur',
    'tojikiston':'dushanbe',
    }
print("Dunyo davlatlari:")
for key in sorted(davlatlar_poytaxtlar.keys()):
    print(f"{key.upper()}")
    
print("Dunyo davlatlari poytaxtlari:")
for value in sorted(davlatlar_poytaxtlar.values()):
    print(f"{value.title()}")
    
    
# 3-savol.

# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring.-
# Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

poytaxt = input("Qaysi davlatni poytaxtini bilishni xoxlaysi?:")
if poytaxt not in  davlatlar_poytaxtlar:
    print(f"Bizda {poytaxt.upper()} bunday malumot yuq")
else:
    print(f"{poytaxt.upper()} ning poytaxti {davlatlar_poytaxtlar[poytaxt]}")
    
    
# 4-savol.

# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. 
# Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

restoran_menusi = {
    'osh':25000,
    'manti':5000,
    'somsa':15000,
    'shashlik':12000,
    'tabaka':25000,
    "sho'rva":20000,
    'beshteks':15000,
    'mastava':12000,
    'shulla':15000,
    "go'sht":40000
    }

print("3 ta taom buyurtma bering.")
buyurtmalar = []
for taom in range(3):
    buyurtmalar.append(input(f"{taom+1}-taom:").lower())
    
for taom in buyurtmalar:
        if taom in restoran_menusi:
            print(f"{restoran_menusi[taom]}")
        else:
            print(f"Bizda {taom} yuq")