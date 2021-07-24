"""
faktöriyel
Bu alıştırmada size bir numara verilir. Sayının faktöriyelini döndürmelisiniz. 
Faktöriyelin o sayıyı altındaki tüm sayılarla çarptığını unutmayın.

5 faktöriyel = 5 * 4 * 3 * 2 * 1

Örnek:

factorial(5) --> 120
factorial(3) --> 6
"""

def factorial(num):
    deger = 1
    for i in range(num):
        deger *= i+1
    return deger

print(factorial(5))