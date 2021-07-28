"""
Listenin ortasına insert_middle eklenen adlı bir işlev yazın x. 
Listede tek sayıda öğe varsa, ortadaki dizini hesaplarken aşağı yuvarlayın.

Not: Sen, işlev her zaman bir liste adı verilecek varsayabiliriz ancak, olabilir değil bu liste boş olmadığını varsayalım.

"""

def insert_middle(yourList: list, x):
    yourList.insert(len(yourList)//2,x)
    return yourList
    
print(insert_middle([0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0], 0))
