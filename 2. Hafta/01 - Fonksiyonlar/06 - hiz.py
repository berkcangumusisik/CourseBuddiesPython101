"""Fizikte, bir nesnenin sabit ivmeyle hareket ederken son hızını 
(veya hızını) bulmak için aşağıdaki denklem kullanılabilir:
vf = vi + at
burada:
vf= son hız
vi= ilk hız
a= hızlanma
t= zaman
İlk hız, ivme ve zaman verildiğinde, son hızı döndürecek bir fonksiyon yazın."""

def sonHiz(vi, a, t):
        return vi + a * t

print(sonHiz(10,2,5))