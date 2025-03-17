# 16-Dars. Nesting (Lug'at ichida lug'at) Amaliyot

# 1-savol

# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang.-
# Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.

ism1 = {
        'ism':'muhammadali eshonqulov',
        't_yil':1981,
        't_joyi':'andijon',
        }

ism2 ={
       'ism':'alisher navoiy',
       't_yil':1441,
       't_joyi':'xirot',
       'umr':60,
       }

ism3 = {
        'ism':'abdulla  qodiriy',
        't_yil':1984,
        't_joyi':'toshkent',
        'umr':44
        }

ism4 = {
        'ism':'erkin vohidov',
        't_yil':1936,
        't_joyi':"farg'ona",
        'umr':80,
        }

ismlar = [ism1, ism2, ism3, ism4]
for ism in ismlar:
    print(f"{ism['ism'].title()} {ism['t_yil']}-yilda,\
          {ism['t_joyi']} da tug'ilgan")
          
          
# 2-savol

# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing.
# For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.

ism1 = {
        'ism':'muhammadali eshonqulov',
        't_yil':1981,
        't_joyi':'andijon',
        }

navoiy ={
       'ism':'alisher navoiy',
       't_yil':1441,
       't_joyi':'xirot',
       'umr':60,
       'asarlari':['xamsa', 'lison ut-Tayr', 'Mahbub Al-Qulub']
       }

qodiriy = {
        'ism':'abdulla  qodiriy',
        't_yil':1984,
        't_joyi':'toshkent',
        'umr':44,
        'asarlar':["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
        }

vohidov = {
        'ism':'erkin vohidov',
        't_yil':1936,
        't_joyi':"farg'ona",
        'umr':80,
        'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
        }
    
shaxslar = [ qodiriy, vohidov, navoiy]

for  shaxs in shaxslar:
    print(f"{shaxs['ism'].title()}ning asarlari:")
    for asar in shaxs.get('asarlar',[]):
        print(f"-{asar}")
        
        
# 3-savol

# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang.  Natijani konsolga chiqaring.

kinolar = {
    'ali':['Terminator','Rambo','Titanic'],
    'vali':['Tenet','Inception','Interstellar'],
    'hasan':['Abdullajon','Bomba','Shaytanat'],
    'husan':['Mahallada duv-duv gap','John Wick']
    }
for ism, kino in kinolar.items():
    print(f"\n{ism.title()}ning sivimli kinolari:")
    for kino in kinolar:
        print(f"{kino}")
        
        
# 4-savol

# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang.-
# Har bir davlat haqida ma'lumotni konsolga chiqaring.

davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,'pul birligi':"rinngit"}
    }

for davlat, info in davlatlar.items():
    print(f"\n{davlat} haqida ma'lumot:")
    print(f"  Poytaxt: {info['poytaxt']}")
    print(f"  Maydoni: {info['maydon']} km²")
    print(f"  Aholisi: {info['aholi']} kishi")
    print(f"  Pul birligi: {info['pul birligi']}")
    
    
# 5-savol

# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat haqida ma'lumot bering.- 
#  Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.

davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,'pul birligi':"rinngit"}
    }

davlat_nomi = input("Davlat nomini kiriting:")
if davlat_nomi in davlatlar:
    info = davlatlar[davlat_nomi]
    print(f"\n{davlat_nomi} haqida ma'lumot:")
    print(f"  Poytaxt: {info['poytaxt']}")
    print(f"  Maydoni: {info['maydon']} km²")
    print(f"  Aholisi: {info['aholi']} kishi")
    print(f"  Pul birligi: {info['pul birligi']}")
else:
    print("Bizda bu davlat haqida ma'lumot yo'q.")