"""
Dizin 2'yi Kaldırın
2. dizinde bulunan değeri kaldırılmış olarak verilen bir dizeyi döndüren 
bir işlev yazın. (Not: Karıştırma her zaman en az 3 karaktere sahip olacaktır.)

"""

def remove_second_index(str):
    if len(str) > 2:
        return str[0:2] + str[2:3].replace(str[2:3],"") + str[3:]
    else:
        return str
print(remove_second_index("Hi"))
print(remove_second_index("Hello"))