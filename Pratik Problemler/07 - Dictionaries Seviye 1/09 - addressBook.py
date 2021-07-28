"""address_book Anahtar olarak kişilerin adlarını ve değerler olarak telefon numaralarını içeren bir 
sözlüğünüz var . Sözlükte bir ismin olup olmadığını kontrol eden ve True
olup olmadığını ve False aksini döndüren bir fonksiyon yazın ."""

def lookup_name(address_book, name):
    if name  in address_book:
        return True
    else:
        return False
