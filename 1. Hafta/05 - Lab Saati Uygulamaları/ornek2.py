"""
Hafta 1 Soru 2
2. Bir üçgen dik mi, ikizkenar mı hesaplayın.

Nelere ihtiyacımız var?

Kullanıcıdan girdi almamız lazım.
Bu girdiyi float türünde kabul etmemiz gerekiyor.
Üçgenin türüne karar vermek için gereken şartları sağlayıp sağlamadığını kontrol eden statementları oluşturmamız gerekiyor.
Dik üçgen olması için aranan şart ne? o Dik kenarlarının karesinin toplamı diğer kenarın karesine eşit olmalı.
İkizkenar üçgen olması için aranan şart ne? o Herhangi iki kenarın uzunluğunun birbirine eşit olması gerekir.
"""

from math import *

print("Kenar uzunluklarını girerken küçükten büyüğe doğru gidiniz.")

k1 = float(input("Birinci kenar uzunluğunu giriniz: "))
k2 = float(input("İkinci kenar uzunluğunu giriniz: "))
k3 = float(input("Üçüncü kenar uzunluğunu giriniz: "))

if (k3 == sqrt(k1**2 + k2**2)):
    print("Kenar uzunlukları {}, {}, {} olan bu üçgen dik üçgendir.".format(k1,k2,k3))
elif (k1 == k2 and k2 != k3) or (k1 == k3 and k3 != k2) or (k2 == k3 and k2 != k1):
    print("Kenar uzunlukarı {}, {}, {} olan bu üçgen ikizkenar üçgendir.".format(k1,k2,k3))
else:
    print("Yanlış bilgi girişi yaptınız. Girdiğiniz kenar uzunlukları herhangi bir üçgen tipine uymuyor.")