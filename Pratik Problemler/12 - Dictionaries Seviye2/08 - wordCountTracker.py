"""Kelime Sayımı İzleyici
Bir metin dizesi verildiğinde, dizede count her kelimenin kaç kez göründüğünü izleyen bir sözlük döndürün.

"""

def word_count(text):
    my_string = text.split()
    count = {}
    for item in my_string:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count
print(word_count("Deneme 1234"))