"""Size bir dosya adı soran, ardından bu dosyayı açan ve dosyanın satırlarını arayarak dosya 
içini okuyan bir kod verildi. Sizden istediğimiz, “X-DSPAM-Confidence: ” değerlerinin ortalamasını 
bulmanız. Örnek bir satır:

X-DSPAM-Confidence: 0,8475
Ardından aşağıda gösterildiği gibi bir çıktı oluşturun. 
Çözümünüzde sum() fonksiyonunu veya sum adlı bir değişken kullanmayın.

İstenilen Çıktı:

Ortalama X-DSPAM-Confidence: 0,7507185185185187


"""

fname = "mbox-short.txt"
fh = open(fname)
total = 0
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence: "):
        total += float(line[line.find(':')+1:])
        count+=1
print("Average X-DSPAM-Confidence:", total/count)
