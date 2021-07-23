""" Ardışık Sayı

Bir sayı ve + veya - alan bir fonksiyon yazın. 
İşlev, ardışık sayıyı, sayıdan önce (-) veya sonra (+) döndürmelidir.

"""

def consecutive_number(number, symbol):
    if symbol == "+":
        number = number +1
        return number
    elif symbol == "-":
        number = number -1
        return number

print(consecutive_number(3,"+"))
print(consecutive_number(-3,"-"))
