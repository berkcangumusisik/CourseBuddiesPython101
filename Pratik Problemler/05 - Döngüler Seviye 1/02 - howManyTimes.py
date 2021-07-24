""" 
Kaç kez
Bu alıştırmada size bir başlangıç ​​değeri, bir bitiş değeri ve bir artış veriliyor. 
Bu parametreler verildiğinde döngünün kaç kez yürütüldüğünü döndürür.

Örnek:

loop_count(3, 10, 3) --> 3
loop_count(5, 15, 1) --> 10

"""
def loop_count(start, end, increment):
    sayac = 0
    for i in range(start, end, increment):
       sayac += 1 
    return sayac
print(loop_count(3, 10, 3))
print(loop_count(5, 15, 1))