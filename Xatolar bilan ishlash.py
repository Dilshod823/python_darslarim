# 35-Dars. Xatolar bilan ishlash.

yosh = input("Yoshingizni kiriting:")
try:
    yosh = int(yosh)
except:
    print("Siz butun son kiritmadingiz")
else:
    print(f"Siz {2025-yosh}-yilda tug'ulgansiz")
    
print("Dastur davom etmoqda")
print("Dastur tugadi")



# Xatolikni aniq qilib kiritib ketish
yosh = input("Yoshingizni kiriting:")
try:
    yosh = int(yosh)
except ValueError:
    print("Siz butun son kiritmadingiz")
else:
    print(f"Siz {2025-yosh}-yilda tug'ulgansiz")
    
print("Dastur davom etmoqda")
print("Dastur tugadi")



# ZeroDevisionError

x,y= 5, 10
try:
    y/(x-5)
except ZeroDivisionError:
        print("0 ga bo'lib bo'lmaydi")
        
        
# IndexError

mevalar = ['olma', 'anor', 'uzum', 'banan']
try:
    print(mevalar[5])
except:
    print(f"Ro'yxatda {len(mevalar)} ta meva bor")



# KeyError

user = {'username':'sariqdev',
        'status':'admin',
        'email':'admin@sariq.dev',
        'phone':'99897123456'}

key = 'tel'
try:
    print(f"Foydalanuvchi: {user[key]}")
except:
    print("Bunday kalit mavjud emas")



# FileNotFoundError

filename = "data.txt" # bunday fayl mavjud emas
try:
    with open(filename) as f:
        text = f.read()
except FileNotFoundError:
    print(f"{filename} mavjud emas")


# Bir nechta xatolar bilan ishlash

n = input("Butun son kiriting: ")
try:
    n = int(n)
    x=20/n
except ValueError: # agar foydalanuvchi butun son kiritmasa
    print("Butun son kiritmadingiz")
except ZeroDivisionError: # agar foydalanuvchi 0 kiritsa
    print("0 ga bo'lib bo'lmaydi")
else:
    print(f"x={x}")







   