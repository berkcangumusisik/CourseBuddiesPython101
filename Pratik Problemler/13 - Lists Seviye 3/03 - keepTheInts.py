"""
Girişleri Saklayın
keep_ints Tamsayı olmayan tüm öğeleri kaldıran bir işlev yazın . 
Örneğin, 2 bir tamsayı olduğu için listede kalır, ancak 'hello'bir dize olduğu için kaldırılır.
Not: Sen, işlev her zaman bir liste adı verilecek varsayabiliriz ancak, 
olabilir değil bu liste boş olmadığını varsayalım.

"""

def keep_ints(my_list):
    return [x for x in my_list if type(x) == int]

print(keep_ints([0, 1.9, 'dog', True]))