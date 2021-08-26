import datetime
import time
import arac
import sqlite3

tc = 0
fiyat = 0


def araba_kirala():
        print("Saatlik araba Kiralama işlemi başlatılıyor....")
        time.sleep(1)
        print("Kiralama başlatıldı!")
        start = datetime.datetime.now()
        now = start.minute
        hesap = input("bitirmek için D")
        if hesap == "D":
            end = datetime.datetime.now()
            after = end.minute

            saat = (after - now) * 0.0166666667
            print(saat, "saat")


            araba1 = arac.Araba()
            fiyat= araba1.a_saatlik * saat
            print(fiyat,"TL")

            return fiyat


def bisiklet_kirala():
    print("saatlik bisiklet Kiralama işlemi başlatılıyor....")
    time.sleep(1)
    print("Kiralama başlatıldı!")
    start = datetime.datetime.now()
    now = start.minute
    hesap = input("bitirmek için D")
    if hesap == "D":
        end = datetime.datetime.now()
        after = end.minute

        saat = (after - now) * 0.0166666667
        print(saat, "saat")

        bisiklet1 = arac.Bisiklet()
        fiyat= bisiklet1.b_saatlik * saat
        print(fiyat,"TL")

        return fiyat

#araba_kirala()
#bisiklet_kirala()