"""Bu alıştırmada, 'beğen' kelimesini 'beğenmeme' ile değiştireceksiniz, eğer 
like kelimesinden sonra bilgisayar kelimesi bulunmazsa, bu durumda 'beğen' 
kelimesini 'love' ile değiştireceksiniz.

Örnek:

replace_like("I like recess") --> "I dislike recess"
replace_like("I like computer science") --> "I love computer science"
"""

def replace_like(phrase):
    if "computer" in phrase:
        return phrase.replace("like","love")
    else:
        return phrase.replace("like","dislike")

print(replace_like("I like recess"))
print(replace_like("I like computer science"))
