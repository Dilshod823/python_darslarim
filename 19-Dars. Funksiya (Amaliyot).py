# 19-Dars. Funksiya (Amaliyot)

# 1-savol.

# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.

ism = input("Ismingiz nima?:")
yosh = input(f"{ism.title()} yoshingiz nechida?:")

def yoshni_hisobla(yosh, ism):
    """foydalanuvchidan ism va yoshini so'rab,
    tug'ilgan yilini hisoblovchi dastur"""
    print(f"{ism.title()} {2025-yosh}-yilda tug'ilgan")
    
yoshni_hisobla(yosh=23, ism='dilshod')


# 2-Savol.

# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.

son = float(input("Bironta son kiriting:"))
def kub_va_kvadratni_hisobla(son):
    """foydalanuvchi kiritgan sonning kvadrat,
    va kubini hisoblovchi dastur"""
    print(f"sonning kvadrati {son**2} ga kubi esa {son**3} ga teng")
    
kub_va_kvadratni_hisobla(son)


# 3-Savol.

# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.

son = float(input("Bironta son kiriting:"))
def sonni_hisobla(son):
    """Foydalanuvchi kiritgan sonning juft,
    yoki toqligini hisoblovchi dastur"""
    if son%2:
        print("Juft son ")
    else:
        print("Toq son ")
        
sonni_hisobla(son)


# 4-Savol.

# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing.-
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.

def kattasini_hisobla():
    """Foydalanuvchi kiritgan sonni kattasini,
    hisoblab chiqaruvchi dastur"""
print("Ikkita son kiriting.")
b_son = float(input("Birinchi son:"))
ik_son = float(input("Ikkinchi son:"))
if b_son<ik_son:
    print(b_son)
elif b_son==ik_son:
    print("sonlar teng")
else:
    print(ik_son)

kattasini_hisobla()


# 5-Savol.

# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz-
# bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.

def bolinish_alomatlari(son):
    """Foydalanuvchi kiritgan sonni qoldiqsiz,
    bo'linuvchilarini topuvchi dastur"""
    for n in range(2, 11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")

bolinish_alomatlari(20)