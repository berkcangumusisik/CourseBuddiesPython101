"""
Çiftler ve Oranlar
Tüm çift sayıları evens_and_odds dizgeye 'even've tüm tek sayıları dizgeye çeviren bir fonksiyon yazın 'odd'. 
Örneğin, orijinal liste öğeyi içeriyorsa 2 işleviniz bu öğeyi 'even'.

Not: Sen, işlev her zaman bir liste adı verilecek varsayabiliriz ancak, olabilir değil bu liste boş olmadığını varsayalım.

"""
def evens_and_odds(my_list):
    for i in range(len(my_list)):
        if my_list[i]  % 2 == 0 :
            my_list[i] = "even"
        else:
            my_list[i] = "odd"
    return my_list

print(evens_and_odds([0, 2, 4, 6]))
print(evens_and_odds([8999, 9000, 9001]))