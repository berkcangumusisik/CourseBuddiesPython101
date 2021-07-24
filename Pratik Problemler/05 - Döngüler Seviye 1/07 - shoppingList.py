"""
Bu alıştırmada size bir alışveriş listesi ve bir eşya verilecektir. 
İade True öğe aksi dönmek, alışveriş listede olup olmadığını False.

Örnek:

shopping_list(["milk", "eggs", "bread"], "milk") --> True
shopping_list(["milk", "eggs", "bread"], "candy") --> False"""

def shopping_list(my_list, item):
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

print(shopping_list(["milk", "eggs", "bread"], "milk"))