# 11-Dars. BIR NECHTA SHARTLARNI TEKSHIRISH (if-elif-else zanjiri va or, and operatori)


# if-elif-else ketma-ketligi
yosh = int(input('Yoshingiz nechida? '))
if yosh<=4:
    print('Sizga kirish bepul.')
elif yosh<=12:
    print('Sizga kirish 5000 so\'m')
else:
    print('Sizga kirish 10000 so\'m')
    
# kodlarni qisqa yozish 
yosh = int(input("Yoshingizni kiriting:"))
if yosh<=4:
    narh=0
elif yosh<=12:
    narh=5000
else:
    narh= 10000
print(f"Sizga kirish {narh} so'm")

# bir nechta elif
yosh = int(input('Yoshingiz nechida? '))
if yosh<=4: # yosh bolalarga bepul
    price = 0
elif yosh<=12: # 4 dan 12 yoshgacha 5000 so'm
    price = 5000
elif yosh<65: # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
    price = 10000
else: # qariyalarga esa 8000 so'm
    price = 8000
print(f"Sizga kirish {price} so'm")

# else qismi yo'q kod (yozish majburiy emas)
yosh = int(input('Yoshingiz nechida? '))
if yosh<=4:
    price = 0
elif yosh<=12:
    price = 5000
elif yosh<65:
    price = 10000
elif yosh>=65:
    price = 8000    
print(f"Sizga kirish {price} so'm")

# AND , OR OPERATORLARI
# OR OPERATORI
kun = input("Bugun qaysi kun:").lower()
if kun == 'shanba' or kun == 'yakshanba':
    print("Bugun dam olish kuni")
else:
    print("Bugun ish kuni")
   
# AND OPERATORI
kun = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))
if kun.lower()=='yakshanba' and harorat>=30:
    print("Cho'milgani ketdik!")
elif kun.lower()=='yakshanba' and harorat<30:
    print("Uyda dam olamiz!")
    
# bir nechta shartlarni ketma-ket bajarish
kun = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))
if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
    print("Cho'milgani ketdik!")
elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
    print("Uyda dam olamiz!")
    
# BOOLEAN MA'LUMOTLAR TURI
narh = 15000 # mijoz 15000 so'mga taom oldi
salat = True # mijoz salat ham oldi
choy = False # mijoz choy olmadi

if choy and salat: # agar mijoz choy va salat ham olgan bo'lsa
    narh = narh + 10000 # narhiga 10000 so'm qo'shamiz
elif choy or salat: # aks holda agar mijoz faqat choy yoki salat olgan bo'lsa
    narh = narh + 5000 # narhiga 5000 so'm qo'shamiz
    
print(f"Jami: {narh} so'm " ) # Yakuniy narhni chiqaramiz

# Shartlarni ketma-ket tekshirish
narh = 15000 # mijoz 15 so'mga ovqat oldi
choy = True
salat = False
non = True
kompot = True
assorti = False
#Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
if choy:   # agar choy olsa
    print("Mijoz choy oldi.")
    narh = narh + 3000
if salat:  # agar salat olsa
    print("Mijoz salat oldi.")
    narh = narh + 5000
if non:    # agar non olsa
    print("Mijoz non oldi.")
    narh = narh + 2000
if kompot: # agar kompot olsa
    print("Mijoz kompot oldi.")
    narh = narh + 5000
if assorti: # agar assorti olsa
    print("Mijoz assorti oldi.")
    narh = narh + 15000
    
print(f"Jami {narh} so'm")

# Ro'yxat tarkibini tekshirish (in operatori)
menu = ['osh','qazonkabob','shashlik','norin','somsa']
ovqat = input("Nima ovqat yeysiz?>>>").lower()
if ovqat in menu:
    print('Buyurtma qabul qilindi')
else:
    print('Afsuski bizda bunday ovqat yo\'q')
    
# not in operatori
menu = ['osh','qazonkabob','shashlik','norin','somsa']
ovqat = input('Nima ovqat yeysiz?>>>')
if ovqat.lower() not in menu:
    print('Afsuski bizda bunday ovqat yo\'q')
else:
    print('Buyurtma qabul qilindi.')
    
# Ikki ro'yxatni solishtirish
menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]

for taom in buyurtmalar:
    if taom in menu:
        print(f"Menuda {taom} bor")
    else:
        print(f"Kechirasiz, menuda {taom} yo'q")
        
# Ro'yxat bo'sh emasligini tekshirish
menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]

if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else: # agar ro'yxat bo'sh bo'lsa
    print("Savatchangiz bo'sh!")
    
    
# AMALIYOT

# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!",-
# agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
son = int(input("Bironta juft son kiriting:"))
if son%2 == 0:
    print("Rahmat")
else:
    print("Bu juft son emas")
    
# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
yosh = int(input("Yoshingiz nechida?>>>"))
if yosh<4 or yosh>60:
    narh = 0
elif yosh<18:
    narh = 10000
else:
    narh = 20000
    
print(f"Sizga kirish {narh} so'm")

# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
print("Ikkita son kiriting")
b_son = float(input("Birinchi sonni kiriting:"))
ik_son = float(input("Ikkinchi sonni kiriting:"))
if b_son == ik_son:
    print("Sonlar teng")
elif b_son < ik_son:
    print(f"{ik_son} dan {b_son} kichik")
else:
    print(f"{ik_son} {b_son} dan katta")
    
# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va-
# foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va-
# qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
mahsulotlar = ['olma', 'anor', 'sabzi', 'banan', 'shaftoli', 'anjir', 'xurmo', 'apelsin', 'ananas', 'bexi', 'gilos']
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}- mahsulotni kiriting:"))
    
if mahsulotlar:
    for mahsulot in mahsulotlar:
        if mahsulot in savat:
            print(f"{mahsulot} do'konimizda bor")
        else:
            print(f"{mahsulot} do'konimizda yo'q")
            
print(savat)

# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda-
# yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa -
# "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
 # print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
  for mahsulot in mavjud_emas:
    print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
  
# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning -
# tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
foydalanuvchilar = ['alijon', 'akmal', 'aslid', 'asad', 'dilshod', 'yulchi']
login = input("Yangi login tanlang:").lower()
if login in foydalanuvchilar:
    print(f"{login} band, yangi login tanlang!")
else:
    print(f"Xush kelibsiz, {login}!")
    
# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 
son = int(input("Istalgan butun son kiriting:"))
for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
        