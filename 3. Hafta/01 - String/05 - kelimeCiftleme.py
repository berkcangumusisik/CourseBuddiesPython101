"""Bu egzersizde size 3 kelimelik bir dizi ve bu üç kelimeden birine karşılık gelen bir sayı verilecek. Verilen sayı sırasındaki kelimeyi iki kez yazdıran bir fonksiyon yazın.



double_word(“one two three”, 3) –> “one two three three”



double_word(“cat dog fish”, 2) –> “cat dog dog fish”

cat->1.sırada

dog->2.sırada

fish->3.sırada,

fonksiyonun ikinci girdisi 2 olduğu için, 2.sıradaki dog iki kez yazdırılmış.

"""

def doubleWord(phrase, ref):
    strList = phrase.split(' ')
    strList.insert(ref - 1, strList[ref - 1])
    for str in strList:
        print(str, end=" ")
    return ''

strVar = "cat dog fish"

print(doubleWord(strVar,1))
print(doubleWord(strVar,2))
print(doubleWord(strVar,3))