"""
PARA SAYACI
Dolar, çeyrek, on sent, nikel ve peni sayısını alan ve toplam para miktarını 
dolar olarak döndüren bir fonksiyon yazın.

Not- Her madeni paranın değeri aşağıdaki tutardır:
- Çeyrek (25 sent/ .25 dolar)
- Dimes (10 sent/ .10 dolar)
- Nikel (5 sent/ .05 dolar)
- Peni (1 cent/ 0.01 dolar)
"""

def total_money(dollars, quarters, dimes, nickels, pennies):
    toplam = dollars * 1 + quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return toplam

print(total_money(1, 4, 10, 20, 100))