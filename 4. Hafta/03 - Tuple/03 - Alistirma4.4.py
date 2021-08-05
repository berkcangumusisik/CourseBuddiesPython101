"""mbox-short.txt dosyasını okumak için bir program yazın ve 
her mesaj için günün saatine göre dağılımı hesaplayın. Saati bularak ve 
ardından iki nokta üst üste kullanarak dizeyi ikinci kez bölerek saati ‘Başlangıç’ satırından 
çıkarabilirsiniz.

Gönderen stephen.marquard@uct.ac.za Cmt 5 Ocak 09 : 14: 16 2008
Her saat için sayıları biriktirdikten sonra, aşağıda gösterildiği gibi saate 
göre sıralanmış sayımları yazdırın.

"""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hcount = dict()                                    
hlst = []                                           

for line in handle: 
    words = line.split()
    if len(words) > 2 and words[0] == 'From':       
        hr = words[5].split(':')                   
        hcount[hr[0]] = hcount.get(hr[0], 0) + 1    
        continue

for k,v in hcount.items():                           
    hlst.append((k,v))                               

hlst.sort()                                         
for k,v in hlst:                                    
    print(k,v)                                       