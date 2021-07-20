"""
Bu egzersizde, size bir alışveriş listesi ve bir eşya verilecek. 
Eğer verilen eşya alışveriş listesinde ise True döndürün, alışveriş listesinde değilse False döndürün.
"""
shop_list = ["süt", "un", "yumurta"]

def alisverisListesi(my_list, item):
    isMatch = False
    if isinstance(my_list, list):
        for i in my_list:
            if i is item:
                isMatch= True
                break
        return isMatch
    else:
        print("Liste Giriniz")
        return None

print(alisverisListesi(shop_list, "süt"))
print(alisverisListesi(shop_list, "un"))
print(alisverisListesi(shop_list, "yumurta"))
print(alisverisListesi(shop_list, "makarna"))