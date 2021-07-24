"""remove_last Listeden son elemanı kaldıran bir fonksiyon yazın .

Not: Sen, işlev her zaman bir liste adı verilecek varsayabiliriz ancak, 
olabilir değil bu liste boş olmadığını varsayalım.

"""

def remove_last(my_list):
    if len(my_list) > 0:
        my_list.pop(-1)
        return my_list
    else:
        return my_list
    
print(remove_last([0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0]))