""""
Sıfırları Filtreleyin
filter_out_zeros Listeden tüm sıfırları kaldıran bir fonksiyon yazın .

Not: Sen, işlev her zaman bir liste adı verilecek varsayabiliriz ancak, 
olabilir değil bu liste boş olmadığını varsayalım.

"""

def filter_out_zeros(my_list):
    val = 0
    try:
        while True:
            my_list.remove(val)
    except ValueError:
        pass
    return my_list

print(filter_out_zeros([0,0,0,0,0,0,0,0]))