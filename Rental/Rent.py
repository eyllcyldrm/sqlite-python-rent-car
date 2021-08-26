import os
import sqlite3
import kullanici_ekle as veritabanı
import arac
import sure
import odeme
import time

class Rent(object):

    def __init__(self,tc):
        self.tc = tc

    def menu(self):
        print("""
        ARAÇ KİRALAMA
        1.ÜCRET BİLGİSİ
        
        2.KAYIT OL
        
        3.GİRİŞ YAP 
        
        * Çıkmak için 'q' ya basın...
        
        """)

    def dogrulama(self):
        self.tc = (input("TC girin: "))
        gir_sifre = input("sifre: ")
        sorgu = "SELECT sifre,ad,soyad FROM kullanici where TC =" + self.tc
        cursor.execute(sorgu)
        sorguSonucu = cursor.fetchall()
        #len(sifre) != 0  ve sifre.__len__() !=0 aynı şeyler
        if sorguSonucu.__len__() !=0 and sorguSonucu[0][0].__contains__(gir_sifre) == True:
            print('Hoşgeldin {} {}'.format(sorguSonucu[0][1],sorguSonucu[0][2]))
            return True
        print("hooooop")
        return rent.dogrulama()

    def islemler(self, odeme):
        rent.updateSorguRun(-odeme)
        yeni_bakiye = rent.getBakiye()
        print(yeni_bakiye)

    def tercihEkranı(self):
        print("Yapmak istediğin işlemi seç:")
        secim = input("Araba için '1', Bisiklet için '2', Bakiye için '3', Sifre güncellemek için '4': ")

        if (secim == "1"):
            rent.gunlukSaatlik(500,"araba")
        elif (secim == "2"):
            rent.gunlukSaatlik(40,"bisiklet")
        elif (secim == "3"):
            secim1 = input("Bakiye görüntülemek için '1', Para eklemek için '2': ")
            bakiye = 0
            if(secim1 == "1" ):
                bakiye = rent.getBakiye()
                print(bakiye)
            else :
                ekle = int(input("ne kadar para ekleyeceksiniz: "))
                rent.updateSorguRun(ekle)
                yeni_bakiye = rent.getBakiye()
                print(yeni_bakiye)
        elif (secim == "4"):
            rent.yeniSifre()
        else:
            print("kardeşim şuraya ayık gelin!")
            return rent.tercihEkranı()

    def yeniSifre(self):
        yeniSifre = input("yeni şifreyi giriniz")
        yeniSifre1 = input("şifrenizi tekrar giriniz")
        if (yeniSifre == yeniSifre1):
            updateSorgu = "UPDATE kullanici SET sifre = " + yeniSifre + " where TC=" + self.tc
            cursor.execute(updateSorgu)
            connection.commit()
            print("şifreniz başarıyla güncellenmiştir")
        else:
            print("sifreleriniz uyuşmuyor")
            return rent.yeniSifre()

    def gunlukSaatlik(self, odeme,arabaMiBisikletMi):
        if(arabaMiBisikletMi == "araba"):
            araba = arac.Araba()
            print(araba)
        else:
            bisiklet = arac.Bisiklet()
            print(bisiklet)

        secim = input("Günlük kiralama için 'G', Saatlik kiralama için 'S'")
        if (secim == "G"):
            rent.islemler(odeme)

        elif (secim == "S"):
            if(arabaMiBisikletMi == "araba"):
                fiyat = sure.araba_kirala()
            else:
                fiyat = sure.bisiklet_kirala()
            rent.islemler(fiyat)

    def updateSorguRun(self,hesap):
        guncelBakiye=rent.getBakiye()
        updateSorgu = "UPDATE kullanici SET bakiye = " + str(guncelBakiye + hesap) + " where TC=" + self.tc
        cursor.execute(updateSorgu)
        connection.commit()

    def getBakiye(self):
        bakiyeSorgu = "SELECT bakiye FROM kullanici where TC = " + self.tc
        cursor.execute(bakiyeSorgu)
        bakiye = cursor.fetchall()
        return int(bakiye[0][0])


tc = 0
veritabanı.create_tbl()
connection = sqlite3.connect("kullanicilar.db")
cursor = connection.cursor()
rent = Rent(tc)
while True:
    rent.menu()
    islem = input("seçmek istedğiniz işlem: ")

    if (islem == "q"):
        print("Program kapıtılıyor....")
        break

    elif (islem == "1"):
        print("Araba kategorisinin fiyat listesi...")
        time.sleep(1)
        araba = arac.Araba()
        print(araba)
        print("Bisiklet kategorisinin fiyat listesi...")
        time.sleep(1)
        bisiklet = arac.Bisiklet()
        print(bisiklet)

    elif (islem == "2"):
        print("Lütfen bekleyin...")
        time.sleep(1)
        veritabanı.add_kullanici()
        print("Kaydınız alındı...\nGiriş ekranından işleminize devam edebilirsiniz...")

    elif (islem == "3"):
          rent.dogrulama()
          rent.tercihEkranı()
