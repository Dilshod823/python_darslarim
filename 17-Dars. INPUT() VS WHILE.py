# 17-Dars. INPUT() VS VHILE

# sonlar va Input()
ism = input("Ismingiz nima? :")
savol = f"Salom, {ism.title()}. Yoshingzi nechida? "
yosh = input(savol)
yosh = int(yosh)
height = input("Bo'yingzi necha metr? ")
height = float(height)

# While
son = 1 # son ga 1 qiymatini beramiz
while son<=5: # toki son 5 dan kichik yoki teng ekan...
    print(son, end=' ') # son ni konsolga chiqaramiz,
    son = son+1 # songa 1 qo'shamiz.
    
# input and while
print("Kiritilgan sonning kvadratini hisoblovchi dastur")
savol = 'Istalgan son kiriting'
savol += "(dasturni tugatish uchun 'exit' deb kiritng) :"
qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(float(qiymat)**2)
print("Dastur tugadi")

# ishora
print("Kiritilgan sonning kvadratini hisoblovchi dastur")
savol = 'Istalgan son kiriting'
savol += "(dasturni tugatish uchun 'exit' deb kiritng) :"
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**2)
print("Dastur tugadi")

# while break
print("Kiritilgan sonning kvadratini hisoblovchi dastur")
savol = 'Istalgan son kiriting'
savol += "(dasturni tugatish uchun 'exit' deb kiritng) :"
while True: # Abadiy sikl
    qiymat = input(savol)
    if qiymat == 'exit':
        break # Dasturni to'xtatish
    else:
        print(float(qiymat)**2)
print('Dastur tugadi')

# for break
sonlar = list(range(1,11))
for son in sonlar:
    if son == 5:
        break
    else:
        print(f"{son} ning kvadrati {son**2} ga teng")
        
# for CONTINUE
sonlar = list(range(1,11))
for son in sonlar:
    if son == 5:
        continue
    else:
        print(f"{son} ning kvadrati {son**2} ga teng")
        
# conyinue while
son = 0
while son<10:
    son += 1
    if son%2 != 0:
        continue
    else:
        print(son)
        
# Abadiy sikl
son = 1
while son>0:
    son += 1
    if son%2 == 0:
        continue
    else:
        print(son)
        
        
# AMALIYOT
# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
savol = "Yaxshi ko'rgan kitoblaringiz nomini kiriting"
savol += "(dasturni to'xtatish uchun 'stop' deb yozing) "
kitob = ' '
while kitob != 'stop':
    kitob = input(savol)
    if kitob == 'stop':
        break
    else:
        print(kitob)
        
        
# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000-
# so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin.-
# Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
savol = "Yoshingizni kiriting :"
savol += "(dasturni to'xtatish uchun 'exit' yoki 'quit' deb yozing) :"
while True:
    yosh = input(savol)
    if yosh.lower() == 'exit' or 'quit':
        break
    
yosh = int(yosh)
if yosh>7:
    narh = 0
elif yosh <=18:
    narh = 2000
elif yosh <= 65:
    narh = 10000
    
print(f"Sizga kirish {narh} so'm")
