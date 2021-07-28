"""Bu alıştırmada, size üç kelimelik bir ifade ve üç kelimeden birine atıfta bulunan 
bir tam sayı veriliyor. İfadeyi, referans kelimeyi iki katına çıkararak döndürün.

Örnek:
“`
double_word(“one two three”, 3) –> “one two three three”
double_word(“cat dog fish”, 2) –> “cat dog dog fish"

"""

def double_word(phrase, ref):
    liste = phrase.split()
    result = []
    for word in liste:
        if liste.index(word) == ref - 1:
            result.append(word)
            result.append(word)
        else:
            result.append(word)
    return " ".join(result)            

print(double_word("one two three", 3))
print(double_word("cat dog fish", 2))