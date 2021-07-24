"""remove_second Listeden ikinci elemanı kaldıran bir fonksiyon yazın .İkinci bir öğe yoksa,
orijinal listeyi döndürün.

Not: Sen, işlev her zaman bir liste adı verilecek varsayabiliriz ancak, 
olabilir değil bu liste boş olmadığını varsayalım.

"""

def remove_second(my_list):
    if len(my_list) > 0:
        if len(my_list) == 1:
            return my_list
        else:
            my_list.pop(1)
            return my_list

    else:
        return my_list
    
print(remove_second([0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0]))
print(remove_second([4]))