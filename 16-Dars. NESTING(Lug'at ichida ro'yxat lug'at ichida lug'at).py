# 16-Dars. NESTING (Lug'at ichida ro'yxat, Ro'yxat ichida lug'at)


# Lug'atlar ro'yxati
car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'korobka':'mexanika'
        }

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':2019,
        'narh':15000,
        'km':20000,
        'korobka':'mexanika'
        }
car = car0
print(f"{car['model'].title()},\
  {car['rang']} rang,\
  {car['yil']}-yil, {car['narh']}$")

car = car1
print(f"{car['model'].title()},\
  {car['rang']} rang,\
  {car['yil']}-yil, {car['narh']}$")

car = car2
print(f"{car['model'].title()},\
  {car['rang']} rang,\
  {car['yil']}-yil, {car['narh']}$")  
  
# Keling, barcha avtolarni bitta ro'yxatga joylaymiz, va for tsikli yordamida birma-bir konsolga chiqaramiz:
cars = [car0, car1, car2]
for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['rang']} rang, "
          f"{car['yil']}-yil, {car['narh']}$")
    
malibus = [] # Malibu moshinalari uchun bo'sh ro'yxat yaratdik
for n in range(10):
    new_car = {
        # har bir yangi mashina uchun lug'at yaratamiz
        'model':'malibu',
        'rang':None, # rangi noaniq
        'yil':2020,
        'narh':None, # narhi belgilanmagan
        'km':0,
        'korobka':'avto'
        }
    malibus.append(new_car)

#for malibu in malibus:
 #   print(malibu)
    
for malibu in malibus[:3]:
    malibu['rang'] = 'qizil'
    
#for malibu in malibus:
 #   print(malibu)
 
for malibu in malibus[3:6]:
    malibu['rang'] = 'qora'
    
for malibu in malibus[6:]:
    malibu['rang'] = 'asfalt rang'
    malibu['korobka'] = 'mexanik'
    
#for malibu in malibus:
 #   print(malibu)
 
for malibu in malibus:
    if malibu['korobka'] == 'avto':
        malibu['narh'] = 40000
    else:
        malibu['narh'] = 35000

for malibu in malibus:
    print(malibu)
    
# Lug'at ichida ro'yxat
dasturchilar = {
    'ali':['python', 'c++'],
    'vali':['html', 'css'],
    'hasan':['php', 'sql'],
    'husan':['python', 'php'],
    'maryam':['c++', 'c#']
    }

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end='')
    for til in tillar:
        print(f'{til.upper()} ', end='')
        

# Lug'at ichida lug'at
hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':"o'rta-maxsus",
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
             'tyil':1999,
             'malumot':'maxsus',
             'tillar':['python','php']}
    }
        
for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()},"
          f"{info['tyil']}-yilda tug'ilgan."
          f"Ma'lumoti: {info['malumot']}. \n")
    for til in info['tillar']:
        print(til.upper())
        
        

# AMALIYOT

# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta-
# ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
ism0 = {
        'ism':'muhammadali',
        'familiya':'eshonqulov',
        'tyil':1985,
        'malumot':'oliy'
        }

ism1 = {
        'ism':'alijon qori',
        'familiya':'abdullayev',
        'tyil':1969,
        'malumot':'oliy',
        }

ism2 = {
        'ism':'jahongirqori',
        'familiya':"ne'matov",
        'tyil':1975,
        'malumot':'oliy'
        }
ismlar = [ism0, ism1, ism2]
for ism in ismlar:
    print(f"{ism['ism'].title()} {ism['familiya'].title()} "
          f"{ism['tyil']}-yilda tug'ilgan  Ma'lumoti: {ism['malumot']}")
    
# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing.-
# For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.
# Har bir muallif uchun lug‘at
ism0 = {
    'ism': 'muhammadali',
    'familiya': 'eshonqulov',
    'tyil': 1985,
    'malumot': 'oliy',
    'asarlari': ['Bolalar tarbiyasi', "Hayot yo'llari"]
}

ism1 = {
    'ism': 'alijon qori',
    'familiya': 'abdullayev',
    'tyil': 1969,
    'malumot': 'oliy',
    'asarlari': ["Qur'on shafoati", "Namozni xushu bilan o'qish"]
}

ism2 = {
    'ism': 'jahongirqori',
    'familiya': "ne'matov",
    'tyil': 1975,
    'malumot': 'oliy',
    'asarlari': ['Tajvid qoidalari', "Qur'on tartili"]
}
# Barcha mualliflarni list ichiga joylaymiz
ismlar = [ism0, ism1, ism2]
# For tsikli orqali ma'lumotlarni chiqaramiz
for muallif in ismlar:
    print(f"{muallif['ism'].title()} {muallif['familiya'].title()} ning mashhur asarlari:")
    for asar in muallif['asarlari']:
        print(f" - {asar}")
    print()  # har muallifdan keyin bo'sh qator

        
# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit,-
# uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang.  Natijani konsolga chiqaring.

# Bo'sh lug'at yaratamiz
sevimli_kinolar = {}

while True:
    # Do'st ismini so'raymiz
    ism = input("Do'stingizning ismini kiriting (yoki 'stop' deb yozib yakunlang): ")

    # 'stop' deb yozilsa, sikl to'xtaydi
    if ism.lower() == 'stop':
        break

    # 3 ta sevimli kino-serialini so'raymiz
    kinolar = []
    for i in range(1, 4):
        kino = input(f"{ism}ning {i}-sevimli kino-seriali: ")
        kinolar.append(kino)

    # Lug‘atga qo‘shamiz
    sevimli_kinolar[ism] = kinolar

# Natijani konsolga chiqaramiz
print("\nDo'stlaringizning sevimli kino-seriallari:")
for dost, kinolar in sevimli_kinolar.items():
    print(f"{dost}: {kinolar}")
    
# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang.-
# Har bir davlat haqida ma'lumotni konsolga chiqaring.
davlatlar = {
    "O'zbekiston":{'poytaxt':'toshkent',
                   'maydon':448978,
                   'aholisi':3700000,
                   'til':"O'zbek tili"
                   },
    "Qozog'iston":{'poytaxt':'astana',
                   'maydon':2724900,
                   'aholisi':2000000,
                   'til':'qozoq tili'
                   },
    "Turkiya":{'poytaxt':'anqara',
               'maydon':783000,
               'aholisi':87000000,
               'til':'turk tili'
               }
    }
for davlat, info in davlatlar.items():
    print(f"\n{davlat.title()}ning poyatxti {info['poytaxt'].title()} \n"
          f" maydoni:{info['maydon']},\n Aholisi:{info['aholisi']},\n"
          f"Tili: {info['til']}")
    
    
# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat haqida ma'lumot-
# bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.
davlat = input("Davlat nomini kiriting: ")
if davlat == davlatlar:
    print(f"\n{davlat.title()}ning poyatxti {info['poytaxt'].title()} \n"
          f" maydoni:{info['maydon']},\n Aholisi:{info['aholisi']},\n"
          f"Tili: {info['til']}")
else:
    print(f"Bizda {davlat} haqida malumot mavjud emas")