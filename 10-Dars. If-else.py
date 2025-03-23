# 10-Dras. If-else

# 1-savil.

# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi -
# harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == 'gm':
        print(f"{car.upper()}")
    else:
        print(car.title())

# 2-savol.

# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != 'gm':
        print(f"{car.title()}")
    else:
        print(car.upper())
        
        
# 3-savol.

# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" -
# xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.

login = input("Login ism kiriting:").title()
if login=='Admin':
    print(f"Xush kelibsiz {login}. Foydalanuvchi ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz {login}!")
    
    
# 4-savol.

# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga-
# teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.

print("Ikkita son kiriting.")

x = float(input("Birinchi sonni kiriting:"))
y = float(input("Ikkinchi sonni kiriting:"))

if x==y:
    print("Sonlar teng")


# 5-savol.

# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son",-
# agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 

son = float(input("Istalgan son kiriting:"))
if son>0:
    print("Musbat son")
else:
    print("Manfiy son")
    
    
