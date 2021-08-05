"""
Kopya Yok
remove_duplicates Tüm kopyaları listeden kaldıran adlı bir işlev yazın .

Not: Sen, işlev her zaman bir liste adı verilecek varsayabiliriz ancak, olabilir değil 
bu liste boş olmadığını varsayalım.

"""

def remove_duplicates(my_list):
    res = []
    for x in my_list:
        if x not in res:
            res.append(x)
    return sorted(res)
print(remove_duplicates([2, 2, 1]))