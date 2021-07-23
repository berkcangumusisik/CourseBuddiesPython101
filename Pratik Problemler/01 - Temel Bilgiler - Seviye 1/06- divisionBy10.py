"""
Bir sayı alan ve sayının 10'a bölünüp bölünemeyeceğini kontrol eden bir 
fonksiyon yazın. Fonksiyon bir boole döndürmelidir.
"""

def divisible_by_ten(num):   
    if num % 10 == 0 :
        return True
    else:
        return False
    
print(divisible_by_ten(10))
print(divisible_by_ten(200))
print(divisible_by_ten(11))
print(divisible_by_ten(3))