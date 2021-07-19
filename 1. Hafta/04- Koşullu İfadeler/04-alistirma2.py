"""0.0 ile 1.0 arasında bir puan istemek için bir program yazın. 
Puan aralık dışındaysa bir hata yazdırın. Puan 0,0 ile 1,0 arasında ise, 
aşağıdaki tabloyu kullanarak bir harf notu yazdırın:

Puan Not

> = 0,9 A

> = 0,8 B

> = 0,7 C

> = 0,6 D

<0,6 F

Kullanıcı aralık dışında bir değer girerse, uygun hata mesajı ve çıkış( quit() ) yapın.

"""

try:
    score = float(input("Enter Score: "))
    if score>=0.0 and score<=1.0:
        if score>=0.9:
            print(score,"A")
        elif score>=0.8:
            print(score, "B")
        elif score >= 0.7:
            print(score, "C")
        elif score >= 0.6:
            print(score, "D")
        elif score<0.6:
            print(score, "F")
    else:
        print("Sayı aralık dışında")
        quit()
except ValueError:
    print("Please enter a number")
