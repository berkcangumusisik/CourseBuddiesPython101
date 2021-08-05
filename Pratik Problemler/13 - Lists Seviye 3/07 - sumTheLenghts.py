"""
Uzunlukları Topla
Bir sum_the_lengths listedeki tüm dizelerin uzunluğunu toplayan adlı bir işlev yazın .

Not: Sen, işlev her zaman bir liste adı verilecek varsayabiliriz ancak, olabilir 
değil bu liste boş olmadığını varsayalım.
"""

def sum_length(my_list):
    length = 0
    for string in my_list:
        length += len(string)
    return length


print(sum_length(["python", "is", "fun"]))