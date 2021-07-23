"""
Değere Bölünebilme
İki tamsayı alan bir fonksiyon yazın. İşlev, ilk tamsayının ikinci tamsayıya 
bölünüp bölünemeyeceğini kontrol edecek ve bir boole değeri döndürecektir.
"""

def divisible(num, divisor):
    if num % divisor == 0: 
        return True
    else:
        return False

print(divisible(10,10))
print(divisible(11,10))