""" 
İçini Çıkarın
Herhangi bir dizenin ilk ve son harflerini döndüren bir işlev yazın. 
(Not: Tüm dizelerde en az 2 karakter olacaktır.)
"""

def remove_inside_characters(str):
    if len(str) > 2:
        return str[0:1] + str[-1]
    else:
        return str
    
print(remove_inside_characters("Hi"))
print(remove_inside_characters("Hello"))