"""Bir atıcının ERA'sı (kazanılan koşu ortalaması), kazanılan koşu sayısı 
ile oyundaki toplam vuruş sayısı (genellikle 9) çarpılarak ve 
ardından atıcının atış yaptığı toplam vuruş sayısına bölünerek hesaplanır.

Oyunda 9 vuruş olduğunu varsayan ve kazanılan koşuları ve vuruş vuruşlarını 
temsil eden iki sayı alan bir fonksiyon yazın. İşlev, ERA'yı döndürmelidir.

"""

def era(earned_runs, innings_pitched):
    return (earned_runs * 9) / innings_pitched

print(era(1,3))