# 33- Dars. Fayllar bilan ishlash.(Pickle)

# Fayllarni o'qish


file = open('D:pi.txt', 'r')
PI = file.read()
print(PI)
file.close()


with open("D:/pi.txt", "r") as file:
    pi = file.read()
    
print(pi)

pi = pi.rstrip()
pi = pi.replace("\n", '')
pi = float(pi)
print(pi)


# Manni qatorma-qator o'zgaruvchiga yuklash
        
talabalar = ['Dilshod norbutayev', 'Muhammadali Xudoyqulov', 'Hayitmurod Xushmurodov']

filename = "D:/python_darslarim/talabalar.txt"  
with open(filename, "r") as file:
  for line in file:
      print(line.strip())

with open(filename) as file:
    talabalar = file.readlines()
    
print(talabalar)

talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar)


# Fayllarga Yozish


faylnomi = 'new_fayl_txt'
ism = 'Akmal Xurramov'
tyil = 2002
with open(faylnomi, "w") as fayl:
    fayl.write(ism+'\n')
    fayl.write(str(tyil)+'\n')
    

faylnomi = 'new_fayl_txt'

with open(faylnomi, 'a') as fayl:
    fayl.write('Asi Sheraxmedov\n')
    fayl.write(str(2000))


# Pickle


import pickle

talaba1 = {'ism':'Akmal ', 'familiya':'Xurramov', "tyil":2002}
talaba2 = {'ism':'Asi', 'familiya':'Sheraxmedov', 'tyil':2003}

with open('info','wb') as file:
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)
    
    
import pickle

with open('info','rb') as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)
    
print(talaba1)
print(talaba2)

