"""
Fibonacci dizisi
Bu alıştırma için, belirli sayıda terim için bir Fibonacci dizisi oluşturacaksınız.
Fibonacci dizisi 0 ve 1 ile başlar, sonraki sayı önceki iki sayının toplamıdır. İşte dizinin bir parçası:

0, 1, 1, 2, 3, 5, 8, 13, ...
2'den büyük bir sayı verildiğinde, dizinin o kadar çok terimini boşlukla ayırarak döndürün.

Örnek:

fibonacci(5) --> "0 1 1 2 3 "
fibonacci(9) --> "0 1 1 2 3 5 8 13 21 "
"""
def fibonacci(terms):
    n1 , n2 , liste = 0, 1, ["0"]
    for a in range(terms-1):
        n1, n2 = n2, n2+ n1
        liste.append(str(n1))
    return " ".join(liste).rstrip() + " "
    
print(fibonacci(5))    
