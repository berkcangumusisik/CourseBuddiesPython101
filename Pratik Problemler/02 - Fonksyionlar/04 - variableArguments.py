""" 
Python'daki bir işlev, *args sözdizimini kullanarak değişken sayıda 
argüman alabilir .

def variable_args(*args):
  return args
  
Bu işlevde, kaç tane sağlanmış olursa olsun, argümanlar bir liste olarak saklanır.

Her zaman kendisine sağlanan son argümanı döndüren bir fonksiyon yazın.

"""

def variable_args(*args):
    return args[-1]

print(variable_args([1], 'hello', 'z', 0))
print(variable_args('arg one', ['arg', 'two'], 3, 'four'))