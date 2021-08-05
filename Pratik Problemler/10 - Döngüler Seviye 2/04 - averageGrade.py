"""Ortalama Not
Bu alıştırmada, size sayısal bir not listesi verilecektir. Bunların ortalama değerini döndürmelisiniz.

Örnek:

find_average([70, 80, 90]) --> 80
find_average([90, 93, 98, 92]) --> 93.25
"""

def find_average(grades):
    toplam = sum(grades)
    adet = len(grades)
    return toplam/adet
    

print(find_average([70, 80, 90]))