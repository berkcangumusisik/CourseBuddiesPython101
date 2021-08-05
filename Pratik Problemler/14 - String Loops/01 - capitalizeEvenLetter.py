"""Çift Harfleri Büyük Harf Yap
İndekslerdeki tüm harflerin büyük olduğu bir dize döndürecek bir işlev yazın."""
def capitalize_even_letters(str):
    result = ""
    index = 0
    for letter in str:
        if index % 2 == 0:
            result += letter.upper()
            index += 1
        else:
            result += letter.lower()            
            index += 1
    return result
    
print(capitalize_even_letters("hello"))