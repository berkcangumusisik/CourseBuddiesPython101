"""2 ile değiştirilmiş sayım
Bu alıştırmada, 2'den başlayıp verilen sayıyla biten 2'şer saniye sayacaksınız. 0 ile biten herhangi bir sayıyı atlamanız gerekir.

Çıktıyı bir dize olarak döndürün.

Örnek:

count_by_two(14) --> "2 4 6 8 12 14 "
count_by_two(10) --> "2 4 6 8 "

"""

def count_by_two(end):
    s = ""
    for i in range(2, end+1):
        if i % 2 == 0:
            if i % 10 != 0:
                s += str(i) + " "
            else:
                continue
    return s
print(count_by_two(10))