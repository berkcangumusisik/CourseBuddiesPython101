"""Boşluksuz Dizi Uzunluğu
Boşluklar hariç bir dizenin uzunluğunu döndüren bir işlev yazın.
"""

def length_no_spaces(str):
    return len(str) - str.count(" ")

print(length_no_spaces(" hello "))