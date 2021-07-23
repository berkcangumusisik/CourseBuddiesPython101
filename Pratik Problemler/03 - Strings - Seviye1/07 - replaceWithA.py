"""  
A ile değiştirin
Size merkezinde sesli harf bulunan 3 harfli kelimeler verilir. 
Kelimeyi 'a' ile değiştirilen sesli harfle döndüren bir işlev oluşturun.

"""

def replace_with_a(str):
    return str.replace(str[1:2],"a")

print(replace_with_a("sey"))