# 21-Dars. Funksiyaga ro'yxat qaytarish. (Amaliyot)

# 1-savol.

# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning -
# birinchi harfini katta harfga o'zgatiruvchi funksiya yozing. 

def katta_harf(matnlar):
     for i in range(len(matnlar)):
         matnlar[i]=matnlar[i].title()   
 
 

ismlar = ["ali", "vali", "hasan", "husan"]
katta_harf(ismlar)
print(ismlar)


# 2-savol.

# Yuoqirdagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradigan qilib o'zgartiring

def katta_harf(matnlar):
     matnlar = matnlar[:]
     for i in range(len(matnlar)):
         matnlar[i]=matnlar[i].title()
     return matnlar
 
ismlar = ["ali", "vali", "hasan", "husan"]
yangi_ismlar = katta_harf(ismlar)
print(ismlar)
print(yangi_ismlar)