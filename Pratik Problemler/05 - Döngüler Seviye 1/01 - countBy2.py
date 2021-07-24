"""
2'ye Kadar Say
Bu alıştırmada, 2'den başlayıp verilen sayı ile biten 2'ye kadar sayacaksınız.

Sayıları boşlukla ayrılmış bir dize olarak döndürmelisiniz.

Örnek:

count_by_two(10) --> "2 4 6 8 10 "
count_by_two(4) --> "2 4
"""

def count_by_two(end):
    s = ""
    for i in range(2, end+1):
        if i % 2 == 0:
            s += str(i) + " "
    return s
print(count_by_two(10))