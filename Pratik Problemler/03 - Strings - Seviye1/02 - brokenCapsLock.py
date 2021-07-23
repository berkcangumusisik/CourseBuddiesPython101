""" 
Kırık Büyük Harf Kilidi
Büyük harf kilidi tuşu bozuk! Verilen bir dizgede tüm büyük harfleri 
küçük harfe ve tüm küçük harfleri büyük harfe çevirecek bir fonksiyon yazın.
Örneğin, verilen dize ise hI mOM!, çıktı şu şekilde olmalıdır:Hi Mom!
"""

def function(str):
    return str.swapcase()

print(function("hI mOM!"))