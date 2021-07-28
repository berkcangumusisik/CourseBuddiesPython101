"""
add_one Listedeki her elemana 1 ekleyen bir fonksiyon yazın .

Not: Geçilen listenin her öğesinin bir tamsayı olduğunu varsayabilirsiniz.

Not: Sen, işlev her zaman bir liste adı verilecek varsayabiliriz ancak, olabilir değil bu liste boş olmadığını varsayalım
"""

def add_one(yourList : list):
    return [x+1 for x in yourList]

print(add_one([41, 41, 41, 41, 41, 41]))
