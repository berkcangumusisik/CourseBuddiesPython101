"""
Çok sayıda insanı ve birkaç grubu alan bir fonksiyon yazın. 
Kişiler gruplara eşit olarak bölünecektir (fazla kişiler olabilir). 
Her gruptaki kişi sayısını döndürün.
"""

def split_groups(num_people, num_groups):
    return num_people // num_groups
print(split_groups(10,5))
print(split_groups(10,3))
print(split_groups(10,2))
print(split_groups(5,1))
print(split_groups(5,2))
print(split_groups(5,3))
