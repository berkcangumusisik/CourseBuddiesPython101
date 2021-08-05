"""Bir tamsayı listesi oluşturun ve bu listede tekrarlayan sayıları listeden kaldıran 
remove_duplicates adlı bir fonksiyon yazın.

Misal:

Girdi: remove_duplicates([2, 2, 1])



Çıktı: [1,2]

"""

def remove_duplicates(num_list):
    try:
        return list(set(num_list))
    except:
        print("Lütfen liste giriniz.")

print(remove_duplicates([2, 2, 1]))
