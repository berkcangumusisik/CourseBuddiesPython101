"""
S Sayısı
Bir dizgede bulunan 'lerin sayısını döndürecek bir işlev yazın (hem büyük hem de küçük harf dahil!)

Örneğin, verilen dize ise Shines çıktı olacaktır 2.
"""

def count_s(str):
    return str.count("S") + str.count("s")

print(count_s("Shines"))