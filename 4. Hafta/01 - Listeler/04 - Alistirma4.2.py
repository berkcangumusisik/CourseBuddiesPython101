""" mbox-short.txt dosyasını açın ve satır satır okuyun. Aşağıdaki satır gibi ‘From’ ile 
başlayan bir satır bulduğunuzda:

From stephen.marquard@uct.ac.za Cmt 5 Ocak 09:14:16 2008
“From” satırını split () kullanarak ayrıştıracak ve satırdaki ikinci kelimeyi 
(yani mesajı gönderen kişinin tüm adresini) yazdıracaksınız. İşlemler tamamlandığında, 
yazdırdığınız kişi sayısını yazdıracaksınız.

İpucu: ‘From:’ ile başlayan satırların tamamını eklemediğinizden emin olun. 
Sadece gönderen ismini ekleyeceksiniz. Sayımın nasıl yazdırılacağını görmek için 
örnek çıktının son satırına da bakın.

Örnek verileri http://www.py4e.com/code3/mbox-short.txt adresinden indirebilirsiniz.

"""


finput = "mbox-short.txt"
f = open(finput).readlines()
count = 0
for line in range(len(f)):
    if f[line].startswith("From"):
        for name in f[line].split():
            if "@" in name:
                count += 1
                print(count,":",name[:])

print(count,"person")
