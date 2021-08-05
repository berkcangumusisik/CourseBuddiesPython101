"""Sözlükleri birleştirin
Sözlüklerin bir listesi verildiğinde, birleştirilmiş tüm anahtarlarının yeni bir Sözlüğünü döndürün.

"""

def combine_dictionaries(dictionary_list):
    d = {}
    for dictionary in dictionary_list:
        for k, v in dictionary.items():
            d[k] = v
            
    return d
