""" Words.txt adlı dosyayı açın, dosyayı okuyun ve dosyanın içeriğini büyük harfle yazdırın. 
Çıktıyı üretmek için words.txt dosyasını kullanın.
"""

filename = "words.txt"
fh = open(filename)
fread = fh.read()
print(fread.upper())