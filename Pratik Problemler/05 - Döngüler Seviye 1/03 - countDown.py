"""
Geri Sayım2 puan
Bu alıştırma için, sağlanan bir başlangıç ​​değerinden geri sayım yapan bir çıktı döndüreceksiniz. 
Her sayı boşlukla ayrılmalıdır.

Örnek:

countdown(10) --> "10 9 8 7 6 5 4 3 2 1 0 "
countdown(5) --> "5 4 3 2 1 0 "

"""

def countdown(start):
    s = ""
    for i in range(start , -1, -1):
        s += str(i) + " "
    return s
print(countdown(10))