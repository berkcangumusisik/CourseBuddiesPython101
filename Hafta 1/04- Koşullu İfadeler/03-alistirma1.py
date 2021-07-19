"""
Brüt ücreti hesaplamak için input() kullanarak kullanıcıdan çalışma saati alın. 
40 saate kadar, her saat başına ücret 10 TL dir. 40 saatin üstündeki saatlerin ücreti 15 TL olmaktadır. 
Girilen saate göre ücreti hesaplayan bir kod yazınız.
Test etmek için 30 saat değerini giriniz, 
sonuç 300 TL çıkmalı, ikincil test olarak 50 değerini giriniz, sonuç 750 TL çıkmalı.

"""
try:
    hrs = float(input("Enter Hours:"))
    if hrs <= 40:
        rate = 10
    else:
        rate = 15
    
    pay = hrs * rate
    print("Your pay:", pay)
except:
    print('Please enter a number')