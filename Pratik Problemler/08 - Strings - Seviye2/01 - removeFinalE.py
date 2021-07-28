"""Bir kelimenin son harfini 'e' ise, ancak yalnızca sondan ikinci harf de bir 'e' 
ise kaldıracak bir fonksiyon yazın. Son harf veya sondan ikinci harf 'e' değilse, dizeyi 
olduğu gibi döndürün.

Örnek:

pleasee returns please
excite returns excite
computer returns computer
"""

def remove_last_e(str):
    if 'ee' in str:
        return str.replace("ee", "e")
        
    else:
        return str
    
print(remove_last_e("pleasee returns please"))
print(remove_last_e("excite returns excite"))