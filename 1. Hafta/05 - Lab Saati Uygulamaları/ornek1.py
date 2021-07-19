"""Python Hafta 1 - 1:
CourseBuddies üniversitesi öğrencilerinin mezun olup olamayacağını göstermek için
bir sistem oluşturmaya çalışıyor.
Öncelikle durumunu öğrenmek isteyen öğrencinin, ismini yaşını ve not ortalamasını
(0 - 100 arası) girmesi gerekiyor (input() fonksiyonu ile kullanıcıdan alıcak).
eğer kullanıcının yaşı 17 ve 21 arasındaysa ve not ortalaması 80 ve üzeri 
ise okulunu tamamlayabilecek.
eğer bu koşulları sağlamıyor ise okulunu tamamlayamayacaktır ve 
duruma göre ekrana bir çıktı gösterecektir (print() fonksiyonu ile)
CourseBuddies Üniversitesinin böyle bir sisteme ihtiyacı var, 
Hadi sen de yardım et"""
try:
    isim = input("İsminizi giriniz:")
    yas = int(input("Yaşınızı giriniz:"))
    ortalama = int(input("Not Ortalaması giriniz:"))

    if(yas>16 and yas <22 and ortalama>79 and ortalama<101):
        print("Sınıfı Geçti")
    else:
        print("Sınıfı Geçemedi")
except:
    print("Lütfen bir sayı giriniz.")