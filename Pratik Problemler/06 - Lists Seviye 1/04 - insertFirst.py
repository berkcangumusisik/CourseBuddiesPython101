""" Listenin ilk elemanı olarak insert_first ' e eklenen adında bir fonksiyon yazın .

Not: Sen, işlev her zaman bir liste adı verilecek varsayabiliriz ancak, 
olabilir değil bu liste boş olmadığını varsayalım.

"""
def insert_first(my_list, x):
    if len(my_list) >= 0:
        my_list.insert(0, x)
        return my_list
print(insert_first([3,4,6], 5))
