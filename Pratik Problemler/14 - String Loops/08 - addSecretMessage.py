"""Gizli Mesaj Ekle6 puan
Verilen bir dizgeye gizli bir mesaj ekleyecek bir fonksiyon yazın. 
Dizede herhangi bir 'y' bulunduktan sonra “gizli” mesajı bir dizeye eklenmelidir.

Örneğin, verilen dize ise bye, döndürülen dize şöyle olmalıdır:bysecrete
"""

def add_secret_message(words:str):
    for letter in words:
        if letter == "y" and "ysecret" not in words:
            words = words.replace("y","ysecret")
    return words
print(add_secret_message("bye"))
print(add_secret_message("hi"))
print(add_secret_message("hey lady"))
