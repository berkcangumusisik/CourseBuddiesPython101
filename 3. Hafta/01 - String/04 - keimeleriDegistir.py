"""Bu alıştırmada size iki kelimeden oluşan bir string(dize) veriliyor. Bu iki kelimenin değiştirildiği bir string(dize) döndürmeniz gerekir.
Örneğin:
print(kelimeDegistir("Golden Bear"))  --> Bear Golden
print(kelimeDegistir("day snow")) -->snow day
"""

def kelimeDegistir(str):
    strList = str.split(" ")
    if len(strList)> 2:
        return "İki kelimeden fazla yazamazsın"
    else:
        return strList[-1] + ' ' + strList[-2]
    
print(kelimeDegistir("Golden Bear"))
print(kelimeDegistir("day snow"))