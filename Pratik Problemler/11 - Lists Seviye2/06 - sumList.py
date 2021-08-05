"""
sum_list Listedeki tüm sayıları toplayan adlı bir fonksiyon yazın .

Not: Sen, işlev her zaman bir liste adı verilecek varsayabiliriz ancak, 
olabilir değil bu liste boş olmadığını varsayalım."""

def sum_list(my_list):
    topla = 0
    for i  in range(len(my_list)):
        topla += my_list[i]
    return topla

print(sum_list([3,3,3]))