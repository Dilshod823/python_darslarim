# 14-Dars. LUG'AT BILAN TAISHUV


# Lug'at bilan ishlash
car_0 = {'model':'ferrari','rang':'qizil'}
print(car_0['model'])
print(car_0['rang'])

talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
print(f"{talaba_0['ism'].title()},\
 {talaba_0['t_yil']}-yilda tu'gilgan,\
 {talaba_0['yosh']} yoshda")
 
# Yangi juftlik qo'shish
talaba_0['kurs'] = 4 # yangi 'kurs' nomli so'zga 4 qiymatini yuklaymiz
talaba_0['fakultet'] = 'iformattika' # 'fakultet' nomli kalitga 'informatika' qiymatini yukladik

# Bo'sh lug'at
talaba_1 = {}
talaba_1['ism'] = 'dilshod norbutayev'
talaba_1['yosh'] = 23
talaba_1['tyil'] = 2002
talaba_1['kurs'] = 3
print(talaba_1)
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['yosh']} yoshda {talaba_1['tyil']}-yilda tug'ilgan")

# qiymatni o'zgartirish
talaba_1['kurs'] = 4 # 'kurs' ni 4 ga o'zgartiramiz.
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# kalit so'z-qiymat juftligini o'chirish
talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
print(talaba_0)
del talaba_0['yosh'] # yosh degan kalit so'z (va qiymatni) o'chiramiz
print(talaba_0)

# Lug'atni qatorlarga bo'lib yozish
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }

# get() metodi
phone = telefonlar['ali']
print(f"Alining telefoni {phone}")

phone = telefonlar.get('hasan','Bunday ism mavjud emas')
print(phone)

phone = telefonlar.get('hasan')
print(phone)


# AMALIYOT

# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni-
# matn shaklida konsolga chiqaring :Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
otam = {'ism':'Bahodir Zokirov', 'yosh':51, 'tyil':1974}
onam = {'ism':'Sanobar Zokirova', 'yosh':46, 'tyil':1980}
opam = {'ism':'Shahnoza Norbutayeva', 'yosh':26, 'tyil':1999}
singlim= {'ism':'Nozima', 'yosh':20, 'tyil':2005}

print(f"Otajonimning ismi {otam['ism'].title()} {otam['yosh']} yoshda {otam['tyil']}-yilda tug'ilgan")
print(f"Onajonimning ismi {onam['ism'].title()} {onam['yosh']} yoshda {onam['tyil']}-yilda tug'ilgan")
print(f"Opamning ismi {opam['ism'].title()} {opam['yosh']} yoshda {opam['tyil']}-yilda tug'ilgan")
print(f"Singlimning ismi {singlim['ism'].title()} {singlim['yosh']} yoshda {singlim['tyil']}-yilda tug'ilgan")

# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin.-
# Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
oilam_taomlar = {'otam':'manti',
                 'onam':"sho'rva",
                 'opam':'somsa',
                 'singlim':'shulla'
                 }
ovqat = oilam_taomlar['otam']
print(f"Otamning sevimli taomi {ovqat}")
ovqat = oilam_taomlar['onam']
print(f"Onamning sevimli taomi {ovqat}")
ovqat = oilam_taomlar['opam']
print(f"Opamning sevimli taomi {ovqat}")

# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo)-
# va har birining qisqacha tarjimasini yozing.
Python_lugat = {
    'print':'dasturni konsolga chiqaradi',
    'string':'matn',
    'integer':'butun son',
    'float':'onlik son',
    'type':"o'zgaruvchida saqlangan malumot turini tekshiradi",
    'input':'foydalanuvchidan biron nima sorashda ishlatiladi',
    'list':"ro'yhat",
    'append':"ro'yhatga element qo'shadi(ro'yxat oxiriga qo'shadi)",
    'insert':"ro'yhatga element qo'shadi(Index bo'yicha ro'yxatga element qo'shadi",
    'del':"ro'yxatdan elementni o'chiradi(qiymat bo'yicha o'chiradi)",
    'remove':"ro'yxatdan elementni o'chiradi(index bo'yicha o'chiradi)",
    'pop':"ro'yxatdan elementni sug'urib olishda ishlatiladi",
    'sort':"ro'yxatni alifbo ketma-ketligida chiqaradi(bunda asl ro'yxat o'zgaradi)",
    'sort(reverse True)':"ro'yxatni alifboga qarshi chiqaradi(bunda asl ro'yxat o'zgaradi)",
    'sorted':"ro'yxatni alifbo ketma-ketligida chiqaradi(bunda asl ro'yxat ozgarmaydi)",
    'reverse':"ro'yxatni alifboga qarshi chiqaradi",
    'range':'malum oraliqdagi sonlar ketma-ketligini yaratamiz',
    'min':'sonlardan tashkil topgan royxatdagi sonlarni eng kichigini konsolga chiqarishda foydalanamiz',
    'max':'sonlardan tashkil topgan royxatdagi sonlarni eng kattasini konsolga chiqarishda foydalanamiz', 
    'sum':'sonlardan tashkil topgan royxatdagi sonlarni ortasini hisoblab konsolga chiqarishda foydalanamiz',
    'tuple':"o'zgaruvchan ro'yxatni o'zgarmas ro'yxatga o'tqazadi"
    }

# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. -
# Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
soz = input("Kalit so'z kiriting: ")
if soz in Python_lugat:
    print(f"{soz} ning tarjimasi: {Python_lugat[soz]}")
else:
    print("Bunday so'z mavjud emas")
