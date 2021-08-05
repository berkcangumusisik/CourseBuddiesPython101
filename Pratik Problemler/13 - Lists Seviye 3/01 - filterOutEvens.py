"""Çift Sayıları Filtreleyin 
filter_out_evens Listeden tüm çiftleri kaldıran bir fonksiyon yazın .

Not: Sen, işlev her zaman bir liste adı verilecek varsayabiliriz ancak, 
olabilir değil bu liste boş olmadığını varsayalım.

"""

def filter_out_evens(my_list):
    ls = []
    for i in my_list:
        if i % 2 == 1:
            ls.append(i)

    return ls

print(filter_out_evens([2,4,5,6,7]))    