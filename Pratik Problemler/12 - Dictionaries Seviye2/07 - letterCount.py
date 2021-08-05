"""
Harf Sayımı
verilen bir dizgede kaç benzersiz harf olduğunu döndüren bir işlev yazın
"""

def letter_count(word):
    unique = []
    for char in word[::]:
        if char not in unique:
            unique.append(char)
    return len(unique)

print(letter_count("Aliiii"))