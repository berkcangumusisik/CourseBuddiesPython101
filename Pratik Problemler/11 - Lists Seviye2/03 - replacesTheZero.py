"""
replace_zeros Adında bir fonksiyon yazın tüm tekrarlarını değiştirir 0s ile  1s

Not: Sen, işlev her zaman bir liste adı verilecek varsayabiliriz ancak, olabilir değil 
bu liste boş olmadığını varsayalım.

"""

def replace_zeros(my_list):
    if 0 in my_list:
        for i in range(len(my_list)):
            my_list[i] = 1
    return my_list
    
print(replace_zeros([0,0,0,0,0,0,0,0]))


