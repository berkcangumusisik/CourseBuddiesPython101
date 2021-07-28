"""
Bu alıştırmada size bir kelime veriliyor. Dizeyi, dizenin ortasına eklenen iki tire 
ile döndürmelisiniz. Dize eşit uzunluktaysa, ortadaki iki tireyi birlikte döndürün. 
Dize tek bir uzunluğa sahipse, iki tire orta harfi çevrelemelidir.

Örnek:

split("even") --> "ev--en"
split("friends") --> "fri-e-nds"
"""

def split(word):
    if len(word) == 2:
        return word[0] + "--" +word[1]
    if not len(word) % 2:
        return word[:len(word)//2] + "--" +word[len(word)//2:]
    else:
        return word[:len(word)//2] + "-" + word[len(word)//2] + "-" + word[len(word)//2+ 1:]
    
print(split("even"))
print(split("friends") )