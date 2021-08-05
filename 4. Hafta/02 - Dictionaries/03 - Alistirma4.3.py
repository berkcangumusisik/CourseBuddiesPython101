""" mbox-short.txt dosyasını okumak için bir program yazın ve en çok e-posta mesajını 
kimin gönderdiğini bulun . Program ‘From’ satırlarını arar ve bu satırların ikinci 
kelimesini postayı gönderen kişi olarak alır. Program, gönderenin posta adresini dosyada 
görünme sayısı ile eşleyen bir Python sözlüğü oluşturur. Sözlük oluşturulduktan sonra program, 
en üretken kaydediciyi bulmak için maksimum döngü kullanarak sözlükten okur.
"""

name = input("Enter file:")
if len(name) < 1 : 
    name = "mbox-short.txt"
handle = open(name)
handleList = list()
count = dict()


for line in handle:
    if line.startswith("From"):
        handleList=line.split()
        count[handleList[1]] = count.get(handleList[1],0) + 1

for i in count:
    if count[i] == max(count.values()):
        print("most repeated mail: ",i,max(count.values()),"times")