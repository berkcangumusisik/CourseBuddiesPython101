"""
Bu alıştırmada, belirli sayıda satır verildiğinde bir yıldız üçgen oluşturabilecek bir dize döndürmelisiniz:

Örnek:

star(3) -->

* 
* * 
* * * 
İpucu: Çıktı dizginize bir satır beslemesi eklemek için dizgeye bir "\n" ekleyin

"""
def star(row):
    myList = []
    for satir in range(row+1):
        myList.append("* " * satir)
    return "\n".join(myList).lstrip("\n")
   

print(star(3))

