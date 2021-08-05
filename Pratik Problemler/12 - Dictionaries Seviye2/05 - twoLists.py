"""İki Liste
İki listeyi bir sözlüğe eşleyen ve yeni sözlüğü döndüren bir işlev yazın.

Örnek:

liste1 = [1, 2, 3]
liste2 = [8, 9, 10]

new_dictionary = {1:8 , 2:9 , 3:10}"""

def map_lists(list1, list2):
    dictionary = dict(zip(list1 ,list2))
    return dictionary

print(map_lists([1, 2, 3],[8, 9, 10]))