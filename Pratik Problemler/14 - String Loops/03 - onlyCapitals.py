"""Sadece Büyük Harfler
Sadece verilen bir dizgede bulunan büyük harfleri döndüren bir fonksiyon yazın.

Örneğin, verilen dize ise Bye Felicia! çıktı olacaktır BF."""

def only_capitals(str):
    result = ""
    index = 0
    for letter in str:
        if letter.isupper():
            result += letter
            index += 1
        else:
            index += 1
    return result
    
print(only_capitals("Bye Felicia!"))