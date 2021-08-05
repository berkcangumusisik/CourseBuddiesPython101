"""Çarpma Listesi
multiply_list Listedeki tüm sayıları çoğaltan adlı bir fonksiyon yazın .

Not: Sen, işlev her zaman bir liste adı verilecek varsayabiliriz ancak, 
olabilir değil bu liste boş olmadığını varsayalım.

"""

def multiply_list(my_list):
    carp = 1
    for i in range(len(my_list)):
        carp *= my_list[i]
    return carp

print(multiply_list([5, 3, 1]))