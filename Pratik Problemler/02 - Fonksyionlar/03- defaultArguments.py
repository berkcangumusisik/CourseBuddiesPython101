""" 
Python'da, onlara işlev tanımında bir değer atayarak varsayılan argümanları 
belirtebilirsiniz.

def greet(name, message = "Good morning")
    return message + " " + name"

greet("Andy") => "Good morning Andy"
Bu bağımsız değişken için herhangi bir değer sağlanmazsa, varsayılan kullanılacaktır.

Ancak yine de bir anahtar sözcük bağımsız değişkeni ileterek varsayılanı 
geçersiz kılabilirsiniz.

greet("Andy", "Good afternoon") => "Good afternoon Andy"
Varsayılan bir argüman alan ve onu döndüren bir fonksiyon yazın.
"""

def default(message = "Good morning"):
    return message 

print(default())
print(default(), "Berkcan")