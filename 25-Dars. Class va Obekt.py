# 25-Dars. Class va Obekt

class Kompyuter:
    def __init__(self, model, ran, hhd, gpu, cpu):
        self.model = model
        self.ran = ran
        self.hhd = hhd
        self.gpu = gpu
        self.cpu = cpu
        
    def info(self):
        inf = f"Model: {self.model}, RAM: {self.ran}, SSD: {self.hhd}, GPU: {self.gpu}, CPU: {self.cpu}"
        return inf
    
mackbook = Kompyuter("Apple Mackbook", "8GB", "512GB", "M1", "M1")

print(mackbook.info())

