"""
Dizin 3'te bulunan karakteri döndüren 
bir işlev yazın. Dizin 3'te karakter yoksa 0 döndürün.
"""

def return_first_character(str):
    if len(str) >= 4:
        return str[3:4]
    else:
        return 0
    
print(return_first_character("Hello"))
print(return_first_character("Hi"))