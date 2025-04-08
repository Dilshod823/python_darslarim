# Klasslar (class)

class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        
    def tanishtir(self):
        return f"Mening ismim {self.ism} familiyam {self.familiya} {self.tyil} yilda tug'ilganman"
        
    def get_name(self):
        return self.ism
    
    def gat_age(self, yil):
        return yil - self.tyil
    
talaba1 = Talaba("Dilshod", "Norbutayev", 2002)
talaba2 = Talaba("Muhammadali", "Xudoyqulov", 2001)
talaba3 = Talaba("Akmal", "Xurramov", 2000)
