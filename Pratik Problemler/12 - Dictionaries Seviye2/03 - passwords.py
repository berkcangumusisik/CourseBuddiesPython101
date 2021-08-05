"""
Şifreler
users Tüm kullanıcı adlarını ve şifreleri takip eden sözlüğe dayanarak bir kullanıcı adı ve şifrenin 
doğru olup olmadığını kontrol eden bir fonksiyon yazın . İşleviniz , verilen kullanıcı adı ve 
şifrenin doğru olup olmadığına bağlı olarak Trueveya geri dönmelidir False.
"""

def check_login(users, username, password):
    return username in users.keys() and users[username] == password
