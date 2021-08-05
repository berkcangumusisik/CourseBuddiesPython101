""" 
Çift Karakterler
Çift dizinde bulunan bir dizgedeki tüm karakterleri döndürecek bir işlev yazın.
"""
def even_letters(str):
    result = ""
    index = 0
    for letter in str:
        if index % 2 == 0:
            result += letter
            index += 1
        else:     
            index += 1
    return result

print(even_letters("Hello"))