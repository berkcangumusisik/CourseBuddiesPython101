""" 
* Kelime havuzu oluşturulacak. Kategoriler belirlenecek.
* Resimler halledilecek.
* Kelime dosyasından kelime alınacak
* Kelime uzunluğu hesaplanacak
* Can sayısı vericez.
* Kullanıcıya hoş geldiniz metni ve hangman logosu eklenecek.
* Kelimelerin uzunluğu en az 7 olsun.
* Kategoriye göre seçim yapılacak.
* Kelime harflerinin olacağı liste oluşturulup ilk olarak _ olacak sonra bulunan harf yazılacak.
* oyun_bitti_mi adında bir değişken oluşturulup while döngüsüne sokulacak.
* Kullanıcıdan harf istenecek.
* Bilinen harf _ ile değiştirilecek. Eğer harf bilemediyse canından -1 azalacak.
* Can 0 olunca oyun biter. Kaybettiniz yazısı eklenir.
* Kazanınca tebrikler kazandınız yazısı
* bir harfe basılınca oyundan çıkabilir.
"""
import random
from hangmanArt import stages, logo
from hangmanWords import canlilar, ulkeler, nesneler, kelimeler


print(logo)
print("------------------------ADAM ASMACA OYUNUNA HOŞ GELDİNİZ-----------------------")

oyunBittiMi = False
can = len(stages) - 1
print("""Kategoriler
1. Canlılar
2. Ülkeler
3. Nesneler
4. Rastgele
""")
kategori = int(input("Bir kategori numarası giriniz: "))
if kategori == 1:
    secilenKategori = random.choice(canlilar)
    kelimeUzunlugu = len(secilenKategori)
elif kategori == 2:
    secilenKategori = random.choice(ulkeler)
    kelimeUzunlugu = len(secilenKategori)
elif kategori == 3:
    secilenKategori = random.choice(nesneler)
    kelimeUzunlugu = len(secilenKategori)
elif kategori == 4:
    secilenKategori = random.choice(kelimeler)
    kelimeUzunlugu = len(secilenKategori)
else:
    print("Yalnış kategori seçtiniz. 1- 4 arasında değer giriniz.")


kelime = ""
for i in secilenKategori:
    if i != " ":
        kelime += "_"
    else:
        kelime += " "

while not oyunBittiMi:
    harf = input("Bir harf girişi yapınız:").lower()
    if harf in kelime:
        print(f"Zaten {harf} harfini tahmin etmiştiniz.")
    for pozisyon in range(kelimeUzunlugu):
        letter = secilenKategori[pozisyon]
        if letter == harf:
            kelime[pozisyon] = letter
        print(f"{' '.join(kelime)}")
        if harf not in kelime:
            print(f"{harf} harfi kelime içerisinde bulunmuyor.")
            can -= 1
            if can == 0:
                oyunBittiMi = True
                print("Oyunu kaybettiniz. Üzgünüz :(")
        if not "_" in kelime:
            oyunBittiMi = True
            print("Oyunu kazandınız. Tebrikler :)")
        print(stages[can])
