"""
Ortalama
Bu alıştırmada, başlangıç ​​değerinden bitiş değerine (her iki bitiş noktası dahil) 
kadar bir dizi sayının ortalamasını döndüreceksiniz.

Örnek:

find_average(10, 20) --> 15
find_average(0, 1000) --> 500
"""

def find_average(start, end):
    ortalama = start -1 + end+1
    ort = ortalama / 2
    return ort
    
print(find_average(10, 20))