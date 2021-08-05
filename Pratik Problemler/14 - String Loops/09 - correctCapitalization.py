"""Doğru Büyük Harf Kullanımı
Bir dize alacak ve her yeni kelimeyi (ilk kelime ve boşluktan sonra gelenler) büyük harf yapacak bir fonksiyon yazın.

Örneğin, verilen dize ise martin luther king jr çıktı olmalıdır Martin Luther King Jr."""

def correct_capitalization(str):
    return str.title()

print(correct_capitalization("martin luther king jr"))