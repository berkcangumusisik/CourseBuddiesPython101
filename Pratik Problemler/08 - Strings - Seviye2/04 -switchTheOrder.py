""" Bu alıştırmada size iki kelimeden oluşan bir dize veriliyor. Bu iki kelimenin değiştirildiği 
bir dize döndürmeniz gerekir.

Örnek:

switch_words("Golden Bear") --> "Bear Golden"
switch_words("day snow") --> "snow day"""

def switch_words(phrase):
    space = phrase.find(' ')
    return phrase[space+1:] + " " + phrase[:space]

print(switch_words("Golden Bear"))