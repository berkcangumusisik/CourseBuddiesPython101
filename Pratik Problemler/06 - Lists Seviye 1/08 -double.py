"""
double Listedeki her elemanı 2 ile çarpan bir fonksiyon yazın .

Not: Geçilen listenin her öğesinin bir tamsayı olduğunu varsayabilirsiniz.

Not: Sen, işlev her zaman bir liste adı verilecek varsayabiliriz ancak, olabilir değil bu liste boş olmadığını varsayalım.
"""

def double(my_list):
    return [x * 2 for x in my_list]

print(double([41, 41, 41, 41, 41, 41]))