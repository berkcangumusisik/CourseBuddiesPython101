"""Bu alıştırmada, belirli sayıda satır verildiğinde bir 
yıldız üçgeni oluşturabilecek bir dize(string) döndürmelisiniz.
Misal:
Girilen Sayı: 3
Çıktı:
*
* *
* * *
İpucu: Bir alt satıra geçmek için “\n” ifadesini kullanın.
"""


def yildiz(satir):
    try:
        for satir in range(satir+1):
            print("*" * satir + "\n")
    except:
        print("Bir sayı giriniz")
        return None


print("Yıldız Üçgeni: ")
yildiz(3)
