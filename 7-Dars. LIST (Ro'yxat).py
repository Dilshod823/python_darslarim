# 7-Dars. LIST (Ro'yxat)

# Aralash ro'yxat

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
ismlar = [] # bo'sh ro'yxat

# list elementlari
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
print("Birinchi meva: ", mevalar[0])
print("Ikkinchi meva: ", mevalar[1])

# Agar list elementlari matn ko'rinishida bo'lsa string metodlari qo'llasak bo'ladi
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
print("Birinichi meva:", mevalar[0].upper())
print("Ikkinchi meva:", mevalar[1].title())

# List elementlari ustida arifmetik amallar bajarish:
narhlar = [12000, 18000, 10900, 22000]
print(narhlar[2] + narhlar[3])

# Pythonda Listning eng oxirgi elementiga -1 indeksi orqali ham murojat qilish mumkin.
# Bu usul Listning uzunligini bilmaganda juda asqotadi.

car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
print(car_models[-1]) # Listning eng oxirgi elementiga -1 bilan murojat qilamiz 


# ELEMENTLARNI QO'SHISH, O'CHIRISH VA O'ZGARTIRISH

# Elementni o'zgartirish
narhlar = [12000, 18000, 10900, 22000]
narhlar[0] = 13000
narhlar[1] = 20000
narhlar[2] = 11000
print(narhlar)

# Yangi element qo'shish
# .append() metodi
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
mevalar.append('tarvuz')
print(mevalar)

cars = []
cars.append('malibu')
cars.append('nexia')
cars.append('cobalt')
cars.append('jetnra')
print(cars)

# .insert() metodi
cars = ['Lacetti', 'Nexia 3', 'Cobalt']
cars.insert(1, 'matiz') # 2-o'ringa yangi qiymat qo'shamiz
print(cars)

# Elementni o'chirish (Indeks bo'yicha elementni o'chirish uchun "del" operatoridan foydalanamiz)
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
del mevalar[1]
del mevalar[3]
print(mevalar)

# Qiymati bo'yicha elementni ochirish uchun .remove() metodidan foydalanamiz
mevalar.remove('shaftoli')
print(mevalar)

hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
hayvonlar.remove("mushuk") # Ro'yxatda 2 ta mushuk bor, ulardan birinchisi o'chadi
print(hayvonlar)

# Elementni sug'urib olish (.pop(indeks))
bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(1) # ro'yxatdan unni sug'urib olamiz
print(" men " + mahsulot + "sotib oldim")
print("Olinmagan mahsulotlar:", bozorlik)


# AMALIYOT

# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
ismlar = ['Ali', 'Aki', 'Asi']

# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 
print(f"Salom {ismlar[0]}, bugun choyxona bormi?\n"
      f"{ismlar[1]}, choyxonaga boramizmi?")

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
sonlar = [2, -3, 3.6, 5]

#Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. -
#Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
sonlar[0] + sonlar[1]
sonlar[2] - sonlar[1]
sonlar[3] = -5
print(sonlar)

# t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning,-
# ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 
t_shaxslar = ['Beruniy', 'Ibn Sino', 'Navoiy']
z_shaxslar = ['Alijon qori', 'Jahongir qori' ]

# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
print(f"Men tarixiy shaxslardan {t_shaxslar.pop(0)} bilan, zamonaviy shaxslardan esa {z_shaxslar.pop(1)} bilan suhbat qilishni xoxlardim")    

# friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 
friends = []
friends.append('Ali')
friends.append('Aki')
friends.append('Asi')
friends.append('Kaki')
friends.append('Yulchi')
print(friends)

# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
friends.remove('Aki')
friends.remove('Asi')
print(friends)

# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.append('Aki')
friends.insert(1, 'Asi')
friends.insert(2, 'Akmal')
print(friends)

# Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan- 
# do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmonlar = friends.pop(1)
mehmonlar = friends.pop(2)
print(friends)
print(mehmonlar)