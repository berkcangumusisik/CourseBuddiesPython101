"""
Öğeleri Toplama
Bir sözlüğün tüm değerlerinin ve anahtarlarının toplamını döndüren bir işlev yazın.

"""

def sum_items(dictionary):
    topla = sum(dictionary.values()) + sum(dictionary.keys())
    return topla

