"""İki sayı alan ve bu iki sayının farkını döndüren, 
her zaman küçük olanı büyükten çıkaran bir fonksiyon yazın."""

def difference(num1, num2):
    if num2 > num1:
        return num2 - num1
    elif num1 > num2:
        return num1 - num2
        
        
print(difference(5,6))
print(difference(6,5))