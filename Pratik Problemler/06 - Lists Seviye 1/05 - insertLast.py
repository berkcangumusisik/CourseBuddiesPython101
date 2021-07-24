""" Alıştırma 4.1.5: Son Ekle
Listenin son elemanı olarak insert_last eklenen adında bir fonksiyon yazın x.

Not: Sen, işlev her zaman bir liste adı verilecek varsayabiliriz ancak, olabilir 
değil bu liste boş olmadığını varsayalım."""

def insert_last(my_list, x):
    if len(my_list) >= 0:
        my_list.append(x)
        return my_list
print(insert_last([3,4,6], 5))
