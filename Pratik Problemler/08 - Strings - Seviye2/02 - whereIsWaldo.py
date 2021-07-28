"""
Belirli bir dizgiyi 'Waldo' dizgisi için arayacak bir işlev yazın (her durumda). Bulunursa 
geri dönün here. Bulunamazsa geri dönün not here.

"""
def find_waldo(str):
    if "waldo" in str:
        return "here"
    elif "Waldo" in str:
        return "here"
    elif "WALDO" in str:
        return "here"
    else:
        return "not here"
