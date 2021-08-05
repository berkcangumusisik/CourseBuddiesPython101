"""
Küçük Dizeleri Filtreleyin
filter_out_small_strings Uzunluğu 4'ten küçük olan tüm dizeleri kaldıran bir işlev yazın .

Not: Sen, işlev her zaman bir liste adı verilecek varsayabiliriz ancak, olabilir değil bu liste boş olmadığını varsayalım.

"""

def filter_out_small_strings(my_list):
    ls = []
    for i in my_list:
        if len(i) >= 4 :
            ls.append(i)
    return ls

print(filter_out_small_strings(['a', 'b', 'c', 'd']))
print(filter_out_small_strings(['small', 'big', 'large', 'tiny']))