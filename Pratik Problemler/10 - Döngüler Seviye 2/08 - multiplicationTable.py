"""
Çarpım tablosu
Bu alıştırmada, 0'dan başlayıp sonuna kadar devam eden bir çarpım tablosu oluşturacaksınız. 
Her sayı sekmeyle ayrılmış (“\t”) olmalı ve dönüş dizginize yeni bir satır eklemek için “\n” 
kullanılmalıdır.

Örnek:

multiply(4) -->

0   1   2   3   4
1   1   2   3   4
2   2   4   6   8
3   3   6   9   12
4   4   8   12  16
"""

def multiply(end):
    ls = [[a for a in range(end+1)]]
    for y in range(1, end+1):
       ls.append([y,y] + [y + y * i for i in range(1, end)])
    s  = " " 
    for sublist in ls:
        s += "\t".join(str(z) for z in sublist)
        s += "\t"
        s += "\n"
    return s
    
print(multiply(4))
