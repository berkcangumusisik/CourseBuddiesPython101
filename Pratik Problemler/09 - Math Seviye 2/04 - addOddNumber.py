"""0'dan belirli bir değere kadar tüm tek değerleri toplayan ve son sayıyı döndüren bir fonksiyon yazın.

Örneğin, verilen değer ise 5, çıktı almak için 1 + 3 + 5 eklersiniz 9."""

def add_odd_values(num):
    total = 0
    for i in range(1,num+1):
        if i % 2 == 1:
            total +=  i
        
    return total

print(add_odd_values(5))    