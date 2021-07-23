""" 
oplam 100'den Az mı
İki sayı alan ve iki sayının toplamının 100'den küçük olup olmadığını kontrol 
eden bir fonksiyon yazın. Fonksiyon bir boole döndürmelidir.
"""

def sum(num1, num2):
    if num1 + num2 < 100:
        return True
    else:
        return False
    
print(sum(11,22))
print(sum(100,0))