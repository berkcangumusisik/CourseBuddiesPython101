"""
Bir sözlük verildiğinde, verilen anahtarı verilen değere güncelleyin.

Örneğin:

karel = {
    'color': 'brown',
    'age': 8
}
Ancak bugün Karel'in doğum günü ise karel['age']güncellenmelidir 9
"""

def update_key(dictionary, key, value):
    dictionary[key] = value
    
    return dictionary