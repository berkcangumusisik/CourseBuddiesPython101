"""Python’da, default(varsayılan) argümanları, fonksiyon tanımında girdilere değer atayarak belirleyebilirsiniz.

Eğer argümana bir girdi karşılık gelmezse, tanımlanan değer kullanılacaktır.

Eğer fonksiyona iki girdiyi de sağlarsanız, varsayılan argümanlar yerine iki girdi kullanılır.

Bir default argümanı olan ve onu döndüren bir fonksiyon yazın.

"""
def sayiEkle(sayi, ekle=2,ekle2=2):
    return sayi + ekle + ekle2

print(sayiEkle(5))
print(sayiEkle(5,5))
print(sayiEkle(5,5,5))
