# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 15-Dars. Dictionary(Lug'at)

# 1-savol

# otam (onam, akam, ukam, va hokazo) degan lug'at yarating
# va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting 
# (ismi, tu'gilgan yili, shahri, manzili va hokazo). 
# Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :
#  Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan

otam = {'ism':'zokirov baxodir', 't_yil':1975, 'yosh':50}
onam = {'ism':'zokirova sanobar', 't_yil':1981, 'yosh':44}
opam = {'ism':'norbutayeva shaxnoza', 't_yil':1999, 'yosh':26}
singlim = {'ism':'norbutayeva nozima', 't_yil':2005, 'yosh':20}

print(f"Otamning ismi {otam['ism'].title()} {otam['t_yil']}-yilda tug'ilgan {otam['yosh']} yoshda")
print(f"Onamning ismi {onam['ism'].title()} {onam['t_yil']}-yilda tug'ilgan {onam['yosh']} yoshda")
print(f"opamning ismi {opam['ism'].title()} {opam['t_yil']}-yilda tug'ilgan {opam['yosh']} yoshda")
print(f"singlimning ismi {singlim['ism'].title()} {singlim['t_yil']}-yilda tug'ilgan {singlim['yosh']} yoshda")


# 2-savol


# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. 
# Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. 
# Kamida uch kishining sevimli taomini konsolga chiqaring: 
# Alining sevimli taomi osh

taomlar = {
    'otam':'osh',
    'onam':"sho'rva",
    'opam':'manti',
    'singlim':'tabaka'
    }
print(f"otamning sevimli ovqati {taomlar['otam']}")
print(f"onaming sevimli ovqati {taomlar['onam']}")
print(f"opamning sevimli ovqati {taomlar['opam']}")
print(f"singlimning sevimli ovqati {taomlar['singlim']}")


# 3-savol

# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 
# 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) 
# va har birining qisqacha tarjimasini yozing.

python_lugat ={
    'string':'matn',
    'integer':'butun son',
    'float':"o'nlik son",
    'tuple':"o'zgarmas lug'at",
    'type':"ro'yxat turini tekshirsish",
    'if':'agar',
    'else':'aks holda',
    'elif':'aks holda agar',
    'append':"ro'yxatga element qo'shadi",
    'del':"ro'yxatdan element o'chiradi",
    'pop':"ro'yxatdan elementni sug'urib oladi"
    }



# 4-savol

# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning 
# tarjimasini yuqoridagi lug'atdan chiqarib bering. 
# Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.

kalit = input("Kalit so'z kiriting:").lower()
if kalit in python_lugat:
     print(f"{kalit.capitalize()} ning tarjimasi {python_lugat[kalit]} ")
else:
     print("Bunday so'z mavjud emas")