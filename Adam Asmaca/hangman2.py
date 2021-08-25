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
import hangmanArt
from hangmanArt import stages, logo
from hangmanWords import canlilar, ulkeler, nesneler, kelimeler

def change_letter(kelime,rastgele_kelime,letter):
    k=rastgele_kelime
    while letter in k:
        s = list(kelime)
        k = "".join(k)
        x = k.find(letter)
        k = list(k)
        k[x]="*"
        s[x] = letter
        kelime = "".join(s)

    return kelime

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
    rastgele_kelime = random.choice(canlilar)
elif kategori == 2:
    rastgele_kelime = random.choice(ulkeler)
elif kategori == 3:
    rastgele_kelime = random.choice(nesneler)
elif kategori == 4:
    rastgele_kelime = random.choice(kelimeler)
else:
    print("Yalnış kategori seçtiniz. 1- 4 arasında değer giriniz.")

print(rastgele_kelime)
kelime = ""
for i in rastgele_kelime:
    if i != " ":
        kelime += "_"
    else:
        kelime += " "

guess_list=[]
while not oyunBittiMi:
    harf = input("Bir harf girişi yapınız:").lower()

    if harf in guess_list:
        print(f"Zaten {harf} harfini tahmin etmiştiniz.")
        pass
    for i,letter in enumerate(rastgele_kelime):
        if letter == harf:
            kelime=change_letter(kelime,rastgele_kelime,letter)
            print(kelime)
            break

        elif harf not in rastgele_kelime:
            print(f"{harf} harfi kelime içerisinde bulunmuyor.")
            can -= 1
            if can == 0:
                oyunBittiMi = True
                print("Oyunu kaybettiniz. Üzgünüz :(")
                break
            else:
                break
    if not "_" in kelime:
            oyunBittiMi = True
            print("Oyunu kazandınız. Tebrikler :)")
            break
    guess_list+=harf
    print(stages[can])



can = len(stages) - 1

