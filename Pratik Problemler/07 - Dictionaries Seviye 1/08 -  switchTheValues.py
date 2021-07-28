"""değerleri değiştirin
Bir sözlük verildiğinde, verilen iki anahtarın değerlerini değiştirin."""

def switch(d, key1, key2):
    d[key1] = key2
    d[key2] = key1
    
    return d