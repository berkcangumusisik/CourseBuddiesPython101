"""Tüm kullanıcı adlarını ve şifreleri takip eden users  adında 
sözlüğe dayanarak bir kullanıcı adı ve şifrenin doğru olup olmadığını 
kontrol eden bir fonksiyon yazın. Fonksiyonunuz, verilen kullanıcı adı ve 
şifrenin doğru olup olmadığına bağlı olarak True veya False dönmelidir.

"""

def check_login(users, username, password):
    return username in users.keys() and users[username] == password