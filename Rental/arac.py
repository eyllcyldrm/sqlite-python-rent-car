class Araba():
    def __init__(self,a_saatlik = 25,a_gunluk = 500):
        self.a_saatlik = a_saatlik
        self.a_gunluk = a_gunluk

    def __str__(self):
        return "Saatlik araba fiyatı : {}\nGünlük araba fiyatı : {}".format(self.a_saatlik,self.a_gunluk)

    def getSaatlik(self):
        return self.a_saatlik

class Bisiklet():
    def __init__(self,b_saatlik = 2,b_gunluk = 40):
        self.b_saatlik = b_saatlik
        self.b_gunluk = b_gunluk

    def getSaatlik(self):
        return self.b_saatlik

    def __str__(self):
        return "Saatlik bisikler : {}\nGünlük bisiklet : {}".format(self.b_gunluk,self.b_saatlik)



