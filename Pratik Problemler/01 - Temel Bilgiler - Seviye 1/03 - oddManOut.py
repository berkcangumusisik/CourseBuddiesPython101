"""
Garip Adam Çıktı
Çok sayıda insanı ve birkaç grubu alan bir fonksiyon yazın.
Kişiler gruplara eşit olarak bölünecektir (fazla kişiler olabilir). 
Çift grupları oluşturduktan sonra kalan kişi sayısını döndürür.
"""

def left_over(num_people, num_groups):
    return num_people % num_groups

print(left_over(10,5))
print(left_over(10,3))
print(left_over(10,2))
print(left_over(5,1))
print(left_over(5,2))
print(left_over(5,3))