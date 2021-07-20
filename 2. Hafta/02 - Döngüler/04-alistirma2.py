"""Kullanıcı 'done' ifadesini girene kadar bir kullanıcıdan sürekli 
olarak tamsayı sayıları isteyen bir program yazın. 'done' girildikten sonra,
sayıların en büyük ve en küçüğünü yazdırın. Kullanıcı geçerli bir numaradan başka bir şey girerse,
onu bir try/except yardımı ile yakalayın ve uygun bir mesaj yazdırın. 
"""


buyukSayi = None
kucukSayi = None
sayilar =[]
while True:
    try:
        sayi = input("Bir sayı giriniz:")
        if sayi == "Done!":
            print("Done!")
            break
        elif int(sayi):
            int(sayi)
            sayilar.append(sayi)
            print(sayilar)
            for sayi in sayilar:
                if buyukSayi is None and  kucukSayi is None:
                    buyukSayi = sayi
                    kucukSayi = sayi
                if buyukSayi < sayi:
                    buyukSayi = sayi
                elif kucukSayi > sayi:
                    kucukSayi = sayi
    except :
        print("Lütfen bir sayı giriniz")
print("En büyük sayı:", buyukSayi)
print("En küçük sayı:", kucukSayi)
