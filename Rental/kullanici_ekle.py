import sqlite3
connection =sqlite3.connect("kullanicilar.db")

cursor=connection.cursor() #köprü kurdum.

def create_tbl():
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS kullanici(TC INT,ad TEXT,soyad TEXT,sifre TEXT,bakiye INT)")
    connection.commit()
    connection.close()

def add_kullanici():
    connection = sqlite3.connect("kullanicilar.db")
    cursor = connection.cursor()
    TC = int(input("TC"))
    ad = input("ad:")
    soyad = input("soyad:")
    sifre = input("şifre:")
    bakiye = int(input("bakiye:"))
    sorgu = "INSERT INTO kullanici(TC,ad,soyad,sifre,bakiye) VALUES(" + str(TC) + ",\"" + ad + "\",\"" + soyad + "\",\"" + sifre + "\"," + str(bakiye) + ")"
    cursor.execute("INSERT INTO kullanici(TC,ad,soyad,sifre,bakiye) VALUES(?,?,?,?,?)",(TC,ad,soyad,sifre,bakiye))
    connection.commit()
    print("bir kayit eklendi")


def kullanici_bilgisi():
    cursor = connection.cursor()
    cursor.execute("SELECT TC,sifre FROM kullanicilar ")
    listele = cursor.fetchall()
    #for y in listele:
        #print(y)
    connection.commit()
    connection.close()










