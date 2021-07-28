"""
Belirli bir sözlüğe bir anahtar ve değer ekleyen bir işlev yazın.

Örneğin, karel'e okul (CodeHS) eklersek,

karel = {
    'color': 'brown',
    'age': 8,
}
o zaman olmalı

{
    'color': 'brown', 
    'age': 8,
    'school': 'CodeHS'
}
"""

def add_key(dictionary, key, value):
    dictionary[key] = value
    return dictionary

