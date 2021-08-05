"""
Kaç Çift?
Bu alıştırmada, size bir sayı listesi verilir. Listedeki çift sayıların sayısını döndürür.

Örnek:

count_even([2, 3, 4 ,5]) --> 2
count_even([0, 6, 9, 11]) --> 1
"""
def count_even(numbers):
    count = 0
    for num in numbers:
        if num == 0:
            continue
        elif num % 2 == 0:
            count += 1
        else:
            continue
    return count
print(count_even([2, 3, 4 ,5]))
