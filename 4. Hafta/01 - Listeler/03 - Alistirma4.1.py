"""romeo.txt dosyasını açın ve satır satır okuyun. Her satırı, split() 
fonksiyonunu kullanarak satırı bir String listesine bölün . Program bir kelime listesi oluşturmalıdır. 
Her satırdaki her kelime için, kelimenin zaten listede olup olmadığını kontrol edin ve eğer listedeyse tekrar eklemeyin. 
Program tamamlandığında, ortaya çıkan kelimeleri alfabetik sıraya göre sıralayın ve yazdırın.
"""

fName = input('Enter your file: ')
fList = open(fName).read().split()
wordList=list()
for el in fList:
    if el not in wordList:
        wordList.append(el)
        
wordList.sort()
print(wordList)

for e in range(len(wordList)):
    print(wordList[e])
