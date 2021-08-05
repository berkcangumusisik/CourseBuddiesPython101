"""Maksimum Değer
Bir sözlüğün maksimum değerini döndüren bir işlev yazın """

def max_value(dictionary):
     return max(dictionary.values())
print(max_value({"Hello" : 7,"hi" : 10, "there" : 45,"at" : 23,"this" : 77}))
print(max_value({3 : 7, 8: 13, 5: 2, 10: 100}))