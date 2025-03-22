# Qiymat qaytaruvchi funksiya. (Amaliyot)

# 1-Savol.

# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi -
# funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)

def mijoz_info(ism, familiya, tyil, yosh, tjoy,   gmail=' ', tel_raqam=None):
    """Mijoz malumotlarni lug'at
    qilib qaytaradigan funksiya"""
    mijoz ={'ism':ism,
            'familiya':familiya,
            'tyil':tyil,
            'yosh':2025-tyil,
            'tjoy':tjoy,
            'gmail':gmail,
            'tel_raqam':tel_raqam}
    return mijoz
mijoz1 = mijoz_info('Dilshod', 'Norbutayev', 2002, 23, 'Surhandaro', 'dnorbutaye95gmail.com', 900312440 )
mijoz2 = mijoz_info('Muhammadali', 'Xudoyqulov', 2001, 24, 'Surhandaro')
mijozlar = [mijoz1, mijoz2]
for mijoz in mijozlar:
    print(mijoz)
    
    
# 2-Savol.

# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring-
# Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.

def mijoz_info(ism, familiya, tyil, yosh, tjoy,   gmail=' ', tel_raqam=None):
    """Mijoz malumotlarni lug'at
    qilib qaytaradigan funksiya"""
    mijoz ={'ism':ism,
            'familiya':familiya,
            'tyil':tyil,
            'yosh':yosh,
            'tjoy':tjoy,
            'gmail':gmail,
            'tel_raqam':tel_raqam}
    return mijoz

mijozlar = []
while True:
    print("\nMijoz ma'lumotlarini kiriting.")
    
    ism = input("Ism:")
    familiya = input("Familiya:")
    tyil = input("Tug'ilgan yil:")
    yosh = input("Yosh:")
    tjoy = input("Tug'ilgan joy:")
    
    gmail = input("Email (ixtiyoriy):")
    if gmail ==' ':
        gmail = None
    
    tel_raqam = input("Telefon raqam (ixtiyoriy):")
    if  tel_raqam == ' ':
        tel_raqam = None
    else:
         tel_raqam = int(tel_raqam)
         
    mijozlar.append(mijoz_info(ism, familiya, tyil, yosh, tjoy,   gmail=' ', tel_raqam=None))
    
    davom_ettirish = input("Yana mijoz kiritasizmi? (yes/no)")
    if davom_ettirish == 'ha':
       continue
   
    print("\nMijoz ro'yxati:")
    for mijoz in mijozlar:
        print(f" {mijoz['ism'].title()} {mijoz['familiya'].title()} {mijoz['tyil']}-yilda "
              f" {mijoz['tjoy'].title()} viloytida tug'ilgan {mijoz['yosh']} yoshda {mijoz['gmail']}"
              f"{mijoz['tel_raqam']}")
    
    

# 3-savol.

# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing

def kattasi(x,y,z):
    """Uchta sonning eng kattasini qaytaruvchi funksiya"""
    return max(x, y, z)

x = float(input("Birinchi sonni kiriting:"))
y = float(input("Ikkinchi sonni kiriting:"))
z = float(input("Uchinchi sonni kiriting:"))

print(f"Eng katta son: {kattasi(x, y, z)}")


# 4-Savol.

# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini,-
# perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing

def aylana_info(radius, pi=3.14159):
    """Aylana ma'lumotlarni qaytaruvchi funksiya"""
    aylana = {'radius':radius,
              'diametr':radius*2,
              'perimetr':radius*2*pi,
              'yuzi':radius**2*pi}
    return aylana
radius = float(input("Aylananing radiusini kiriting:"))
natija = aylana_info(radius)

print(natija)


# 5-savol.

# Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga-
# va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)

def tub_sonlar_top(min, max):
    """Tub son qaytaruvchi funksiya"""
    tub_sonlar = []
    for n in range(min, max+1):
        tub = True
        if (n==1):
            tub = False
        elif (n==2):
            tub = True
        else:
            for x in range(2,n):
                if n % x == 0:
                    tub = False
        if tub:
            tub_sonlar.append(n)
            
    return tub_sonlar
min = int(input("Minumum sonni kiriting:"))
max = int(input("Maxsimum sonni kiriting:"))

natija = tub_sonlar_top(min, max)
print(f"{min} dan {max} gacha bo'lgan tub sonlar: {natija}")


# 6-savol.

# Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing. 

def fibonacci(n):
    """sonning fibanacci qiymatini qaytaruvchi funksiya"""
    sonlar = []
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
            return sonlar
        
n = int(input("Fibonacci ketma-ketliging elementini chiqaramiz:"))
print(fibonacci(n))