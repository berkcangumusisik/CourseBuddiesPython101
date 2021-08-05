"""Bir length_of_strings dizi listesini, orijinal listedeki dizilerin uzunluklarının bir 
listesine dönüştüren adlı bir işlev yazın . Örneğin, liste ['hello'] dönüştürülür [5]

Not: Geçirilen listenin her öğesinin bir dize olduğunu varsayabilirsiniz.

Not: Sen, işlev her zaman bir liste adı verilecek varsayabiliriz ancak, olabilir değil 
bu liste boş olmadığını varsayalım.

"""
def length_of_strings(my_list):
    num_words = len(my_list)
    num_words_list = []
    for i in my_list:
        num_words_list.append((len(i)))
    return num_words_list

print(length_of_strings(['hello', 'goodbye', 'hi', 'bai', 'bye', 'whatup']))