"""
Dışarıyı Çıkarın

İlk ve son harfleri kaldırılmış bir dize döndüren bir işlev yazın. 
(Not: Tüm dizeler en az 2 karakterden oluşacaktır.)
"""

def remove_outside_characters(str):
    return str[0:1].replace(str[0:1], "") + str[1:-1] + str[-1].replace(str[-1], "")


print(remove_outside_characters("Hi"))
print(remove_outside_characters("Hello"))
