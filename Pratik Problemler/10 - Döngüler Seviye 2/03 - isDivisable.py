"""Bölünebilir mi?4 puan
Bu alıştırmada size bir bitiş değeri ve bir bölen veriliyor. Bölen ile bölünebilen 
pozitif tam sayıların sayısını bitiş değeri dahil olmak üzere döndürür.

Örnek:

is_divisible(10, 2) --> 5
is_divisible(10, 3) --> 3

"""
def is_divisible(end, divisor):
    count = 0
    for i in range(1 , end+1):
        if i % divisor == 0:
            count += 1
        else:
            continue
    return count


print(is_divisible(10, 2))
