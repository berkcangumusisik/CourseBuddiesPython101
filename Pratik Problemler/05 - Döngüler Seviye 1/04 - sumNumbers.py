"""
Bir başlangıç ​​değeri, bitiş değeri ve bir artış değeri verildiğinde, 
aralıktaki (bitiş noktaları dahil) tüm sayıları toplayın.

Örnek:

sum(0, 10, 2) --> 30 # 2 + 4 + 6 + 8 + 10
sum(25, 30, 5) --> 55 # 25 + 30
"""

def sum(start, end, increment):
    total = 0
    for i in range(start, end+1, increment):
        total += i
    return total

print(sum(0, 10, 2))