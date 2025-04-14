# 9-Dars. FOR takrorlash operatori

mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(mehmon)
    
# For qanday ishlaydi?
mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon} sizni 20-dekabr kuni nahorgi oshga taklif qilamiz\n"
          f"Hurmat bilan, Palonchiyevlar oilasi")
    
mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(mehmon)
    
print(mehmonlar)

# for yordamida sonli ro'yxatlar bilan ishlash
sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")
    
# For yordamida yangi ro'yxat shakllantirish
sonlar = list(range(11))
sonlar_kvadrati = []
for son in sonlar:
    sonlar_kvadrati.append(son**2)
    
print(sonlar)
print(sonlar_kvadrati)

# For va Input
dostlar =[]
print("5 ta eng yaqin do'stingzi kim?")
for dost in range(5):
    dostlar.append(input(f"{dost+1}-do'stingiz kiriting:"))
print(dostlar)


# AMALIYOT

# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
ismlar = ['Ali', 'Aki', 'Asi', 'Adi', 'Yulchi']
for ism in ismlar:
    print(f"Assalomu alaykum {ism.title()} do'stim, Yaxshimisz!")
    
# Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan-
# xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
print(f"kod {len(ismlar)} marta takrorlandi")

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
toq_sonlar = list(range(10,100,3))
for son in toq_sonlar:
    print(f"{son} ning kubi {son**3} ga teng")
    
# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
print("5 ta sevimli kino nomini kiriting")
kinolar =  []
for n in range(5):
    kinolar.append(input(f"{n+1}-kino nomini kiriting:"))
print(kinolar)

# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har-
#  bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
suhbatdoshlar = int(input("Bugun necha kishi bilan suhbat qildizngiz?>>>"))
ismlar = []
for n in range(suhbatdoshlar):
    ismlar.append(input(f"{n+1}-Suhbatdoshingiz kim edi: "))
print(ismlar)