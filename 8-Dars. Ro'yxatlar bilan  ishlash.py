# 8-Dars. Ro'yxatlar bilan ishlalsh


# Ro'yxatni tartiblash (.sort())

cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
print(cars)
cars.sort()
print(cars)

cars = ['Bmw','mercedes benz', 'volvo', 'gm', 'tesla', 'audi']
cars.sort()
print(cars)

# Ro'yxatni alifbo ketma-ketligiga qarshi tartiblash (.sort(reverse=Tue))
cars.sort(reverse=True)
print(cars)

# Asl ro'yxatni o'zgartirmagan holda Alifbo ketma-ketligida tartiblash (.sorted())
mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)

# Asl ro'yxatni o'zgartirmagan holda Alifbo ketma-ketligiga qarshi tartiblash (.reverse=True())
mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
print(sorted(mehmonlar, reverse=True))

# Sonlarni tartiblash
ages = [12, 98, 21, 45, -25]
ages.sort()
print(ages)
print(sorted(ages, reverse=True))


# Royxatni aylantirish (.reverse())
fruits = ['pear','banana','apple','watermelon','lemon']
fruits.reverse()
print(fruits)

# Ro'yxatni uzunligini bilish (len())
fruits = ['pear','banana','apple','watermelon','lemon']
print("Elementlar soni:",len(fruits)) # len(fruits) ro'yxat uzunligini qaytaradi

# .range() Funksiyasi
sonlar = list(range(0, 10))
print(sonlar)

# .renge() funksiyasi yordamida qadamni berish
juft_sonlar = list(range(0, 20, 2))
toq_sonlar = list(range(1, 20, 2))
print("Juft sonlar:", juft_sonlar)
print("Toq sonlar:", toq_sonlar)

# Sonli ro'yxat ustida sodda amallar (min(), max(), sum())
narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
arzon = min(narhlar)
qimmat = max(narhlar)
yigindi = sum(narhlar)
print("Eng arzon:", arzon, "eng qimmat:", qimmat, "Yig'inndi:", yigindi)

# Ro'yxatni kesish
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
my_cars = cars[0:4] # 0-indeksdan boshlab 3 ta element ajratib oladi
print(my_cars)
print(cars[2:5]) # 2-3-4-elementlarni ajratib olamiz (5 kirmaydi)
print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi

# Ro'yxatdan nusxa olish
sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
sonlar2 = sonlar[:]# ro'yxatni to'liq ko'chirib oladi
sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
print("Bu sonlar ro'yxati:", sonlar)
print("Bu sonlar2 ro'yxati:", sonlar2)

# Tuples - O'zgarmas ro'yxat
tomonlar = (20, 30, 55.2)
print(tomonlar)

toys = ('bus','car','bear','dino','snake','lizard')
print(toys[0])
print(toys[-1])
print(toys[2:5])


# O'zgarmas ro'yxatni o'zgaruvchan ro'yxatga o'tqazish (list())
toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# Ro'yxatga o'zgartirishlar kiritamiz
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqueen'
toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
print(toys)


# AMALIYOT

# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar = ["O'zbekiston", "Qozog'iston", "Qirg'iziston", "Turkiya", "Tojikiston"]
print(davlatlar)

# Ro'yxatning uzunligini konsolga chiqaring
print(len(davlatlar))

# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(sorted(davlatlar))

# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
davlatlar = ["O'zbekiston", "Qozog'iston", "Qirg'iziston", "Turkiya", "Tojikiston"]
print(sorted(davlatlar, reverse=True))

# Asl ro'yxatni qaytadan konsolga chiqaring
print(davlatlar)

# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse()
print(davlatlar)

# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
juft_sonlar = list(range(120, 1200, 2))
print(juft_sonlar)

# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
print(sum(juft_sonlar))

# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
kichik = min(juft_sonlar)
katta = max(juft_sonlar)
print(katta - kichik)

# Ro'yxatdagi elementlar sonini hisoblang
print(len(juft_sonlar))

# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
bosh = juft_sonlar[:21]
oxir = juft_sonlar[520:]
orta = juft_sonlar[249:291]
print("boshi:\n", bosh, "oxiri:\n", oxir, "orta:\n", orta)

# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['osh', 'manti', 'shashlik', 'tabaka', 'beshteks']

# nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]

# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove('manti')
nonushta.remove('shashlik')
nonushta.insert(0, "go'sht")
nonushta.append("lag'mon")

# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(nonushta)
print(taomlar)

# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
nonushta[0] = 'qaymoq'
