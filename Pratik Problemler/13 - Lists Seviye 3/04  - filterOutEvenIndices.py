"""Çift Endeksleri Filtreleyin
filter_out_even_indices Eşit bir dizinde oluşan tüm öğeleri kaldıran bir işlev yazın . 
Başka bir deyişle, [0, 2, 4, 6, vb…] dizinlerindeki tüm öğeleri kaldırın, 
ancak öğeleri [1, 3, 5, 7, vb…] dizinlerinde tutun.

Not: Sen, işlev her zaman bir liste adı verilecek varsayabiliriz ancak, 
olabilir değil bu liste boş olmadığını varsayalım.

"""
def filter_out_even_indices(my_list):
    ls = []
    for i in range(1,len(my_list),2):
        ls.append(my_list[i])
    
    return ls

print(filter_out_even_indices([0, 2, 4, 6, 8]))
