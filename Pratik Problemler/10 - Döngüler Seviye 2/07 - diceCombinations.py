"""
Zar kombinasyonları
Bu alıştırmada size 2 ile 12 arasında bir sayı veriliyor. Bu kombinasyonu atabilecek olası iki zar 
kombinasyonunun sayısını döndürmelisiniz. Örneğin, 4 verilirse, 1 ve 3, 2 ve 2 veya 
3 ve 1 atabileceğiniz için 3 döndürürsünüz.

Örnek:

dice_combo(4) --> 3
dice_combo(7) --> 6
"""

def dice_combo(target):
    dA = 1
    dB = 1
    count = 0
    while dA < target:
        while dB < target:
            dB += 1
        dA += 1
        count += 1
    if target < 8:
        return count
    elif target == 8:
        return count-2
print(dice_combo(4))
print(dice_combo(7))