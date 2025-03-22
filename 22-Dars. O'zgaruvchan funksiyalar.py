# 22-Dars. O'zgaruvchan funksiyalar. (*args, **kwargs). [Amaliyot]

# 1-savol.

# Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing

def son_kopaytmasi(*sonlar):
    """Sonlarning ko'paytmasini qaytaruvchi funksiya"""
    qiymat = 1
    for son in sonlar:
        qiymat *= son
    return qiymat

print(son_kopaytmasi(2, 3, 4))  
print(son_kopaytmasi(5, 6))
print(son_kopaytmasi(10))       
print(son_kopaytmasi())


# 2-savol.

# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. Talabaning ismi va familiyasi majburiy argument,-
# qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.

def talaba_info(ism, familiya, **malumotlar):
    """Talaba malumotlarini qabul qilib lug'at ko'rinishida qaytaruvchi funksiya"""
    malumotlar['ism']=ism
    malumotlar['familiya']=familiya
    return malumotlar
talaba1 = talaba_info('Dilshod', 'Norbutayev', tyil=2002, tjoy='Surhandaryo', yosh=23)
talaba2 = talaba_info('Muhammadali', "Xudoyqulov", tel_raqam=900312440, gmail='ali.gmail.com')
   