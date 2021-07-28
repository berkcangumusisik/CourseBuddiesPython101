"""
Verilen anahtarı verilen sözlükten silecek bir fonksiyon yazın
"""

def delete_key(dictionary, key):
    dictionary.pop(key)
    
    return dictionary