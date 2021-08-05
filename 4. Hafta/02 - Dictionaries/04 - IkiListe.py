"""İki listeyi bir sözlüğe eşleyen ve yeni sözlüğü döndüren bir işlev yazın.

Misal:

list1 = [1, 2, 3]

list2 = [8, 9, 10]

new_dictionary = {1:8 , 2:9 , 3:10}"""

def two_list(list1, list2):
    new_dict = dict()
    if len(list1)!=len(list2):
        raise IndexError
    for key in list1:
        new_dict[key] = list2[list1.index(key)]
    return new_dict


l1 = [1,2,3]
l2 = [4,5,6]
print(two_list(l1, l2))