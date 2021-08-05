"""
İyinin Başına Hazırla
prepend_good Listenin her öğesinin başına “good” dizesini getiren bir işlev yazın .

Not: Geçirilen listenin her öğesinin bir dize olduğunu varsayabilirsiniz.

Not: Sen, işlev her zaman bir liste adı verilecek varsayabiliriz ancak, olabilir 
değil bu liste boş olmadığını varsayalım.
"""
def prepend_good(my_list):
    ls = []
    for i in range(len(my_list)):
        ls.append("Good " + my_list[i])
    return ls
print(prepend_good(["1","2","3"]))