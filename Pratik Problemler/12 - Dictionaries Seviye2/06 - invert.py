"""
Tersine Çevir
Anahtarların verilen sözlükteki değerler olduğu ve değerlerin verilen sözlükteki 
anahtarların listeleri olduğu bir sözlük döndüren bir fonksiyon yazın.
"""

def invert(dictionary):
    my_dict = dict([(i,[]) for i in set([value for key,value in dictionary.items()])])
    [my_dict[value].append(key) for key,value in dictionary.items()]
    return my_dict