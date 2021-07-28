"""0'dan belirli bir değere kadar tüm değerleri toplayan ve son sayıyı döndüren bir fonksiyon yazın.

Örneğin, verilen değer ise 4  1 + 2 + 3 + 4 ekleyerek çıktısını alırsınız 10."""

def add_all_values(num):
    toplam = 0
    for i in range(1,num+1):
        toplam += i
        
    return toplam

print(add_all_values(4))