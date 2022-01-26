# Python Sql Kütühanesi Ekleme ; "pip" komutu ile bunu yapıyoruz daha sonra projenin en üst kısmından import komutu ile kullanıyoruz.

# Kütüphaneyi Kullanma
import pymysql.cursor

#Veritabanı bağlantısı
db=pymysql.connect(host='localhost')
user='root',
password='',
db='yemektarifleri',
charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor)

baglanti=db.cursor()


# Kullanıcıdan Yemek Adı ve Tariflerini Alan Kodlar

print(" Yemek Tariflerine Hoşgeldiniz :)")

# Gerekirse Kullanılabilecek Kodlar
#yemek=input("Yemek Adı Giriniz =")
#ymktarifi=input("Yemek Tarifini Yazınız=")

# Alınan Bilgileri txt Dosyasına Yazdırma

kayıt = open("yemektarifleri.txt", "w") 
kayıt.write(input(  "Yemek Adı Giriniz = " )) 
kayıt.write(input( "Yemek Tarifi Giriniz = " ))
kayıt.close()

dosya = open("yemektarifleri.txt","r",encoding="utf-8")
oku = dosya.read()
print("Yemek Adı ve Tarifiniz = " ,oku)