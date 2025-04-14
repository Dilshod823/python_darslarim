# 5-Dars. String (Matn)

shahar = "Қўқон"
viloyat = 'Фарғона'

matn = "Men yangi 📱 oldim"
print(matn)

# STRING USTIDA AMALLAR

# Matnlarni qo'shish opertatori (+)
ism = 'Ahmad'
familiya = 'Qayum'
print(ism + familiya)

ism = 'Ahad'
familiya = 'Qayum'
print(ism + ' ' + familiya) # ikki o'zgaruvchi orasiga bo'sh joy qo'shamiz

# f-string
ism = 'Ahad'
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif)

ism = "James"
familiya = 'Bond'
print(f"Salom, mening ismim {ism}. {ism} {familiya}!")

# Maxsus belgilar
print('Hello World!')
print('Hello \tWorld!')
print('Hello \nWorld!')

# STRING METODLARI

# upper() va lower() metodlari
# upper() metodi matndagi har bir harfni katta harfga o'zgartiradi. 
ism = 'Ahad'
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.upper())

# lower() metodi esa aksincha, har bir harfni kichik harfga o'zgartiradi.
ism = 'Ahad'
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.lower())

# title() va capitalize() metodlari
# title() metodi matndagi har bir so'zning birinchi harfini katta harf bilan yozadi.
ism_sharif = 'james bond'
print(ism_sharif.title())

# capitalize() esa faqatgina eng birinchi so'zning birinchi harfini katta bilan yozadi.
ism_sharif = 'james bond'
print(ism_sharif.capitalize())

# Metodlarni matnlarga qo'llash
print('james bond'.upper())


# strip(), rstrip() va lstrip() metodlari
# Bu metodlar matnning boshi va oxiridagi bo'sh joylarni olib tashlaydi.

#lstrip() — matn boshidagi bo'shliqni,
#rstrip() – matn oxiridagi bo'shliqni,
#strip() — matn boshi va oxiridagi bo'shliqlarni olib tashlaydi
meva = "     olma     "
print("Men " + meva.lstrip() + " yaxshi ko'raman")
print("Men " + meva.rstrip() + " yaxshi ko'raman")
print("Men " + meva.strip() + " yaxshi ko'raman")
print("Men " + meva + " yaxshi ko'raman")


# INPUT —FOYDALANUVCHI BILAN MULOQOT
ism = input("Ismingiz nima?")
print("Assalom alaykum, " + ism.title())

# Keling yuqoridagi kod va uning natijasini chiroyliroq ko'rinishga keltiramiz.
ism = input("Ismingiz nima?\n>>>") # Foydalanuvchi ismini yangi qatordan kiritadi
print("Assalom alaykum, " + ism.title())


# AMALIYOT

# Quyidagi o'zgaruvchilarni yarating: 
kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Sanarqand"

# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang.-
# Va avvalgi mashqni takrorlang.
kocha = input("Ko'changiz nomi? :")
mahalla = input("Mahallangiz:")
tuman = input("Tumaningiz:")
viloyat = input("Viloyatingiz:")
print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
print(f"{kocha} ko'chasi,\n {mahalla} mahallasi,\n {tuman} tumani,\n {viloyat} viloyati")

