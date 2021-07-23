"""
Nakliye Maliyetleri
Yeni bir firma için kargo ücretini firmadan mil olarak ve 
kargo süresini gün olarak hesaplayacak bir fonksiyon yazınız. 
Nakliye maliyeti kuralları aşağıdaki gibidir:
Nakliye mil başına 50 sent
Müşteriler, ürünleri için bekleyecekleri her gün için 10 sent tasarruf eder 
(yani: 1 gün- .10 tasarruf, 2 gün- .20 tasarruf, 3 gün, .30 tasarruf vb.)"""

def calculate_shipping(miles, days):
    return miles * 0.5 - days * 0.1

print(calculate_shipping(100, 0))
