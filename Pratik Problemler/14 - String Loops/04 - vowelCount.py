""" 
Ünlü Sayısı
Belirli bir dizedeki küçük sesli harflerin ( a, e, i, o, ve u) sayısını sayacak bir işlev yazın .

"""
def isVowel(ch):
    return ch in ['a', 'e', 'i', 'o', 'u']

def count_vowels(str):
    str.lower()
    count = 0
    for i in range(len(str)):
        if isVowel(str[i]):
            count += 1

    return count

print(count_vowels("hEllo"))
print(count_vowels("I.O.U"))