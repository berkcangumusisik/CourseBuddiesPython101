def main():
    while True:
        try:
            basamak = int(input("Lütfen basamak sayısı giriniz:"))
            break
        except:
            print("Bir sayı giriniz.")
            
    for i in range(1, basamak+1):
        bosluk(basamak -i)
        kare(i)
        bosluk(1)
        kare(i)
        print()
    
def bosluk(adet):
    print(" " * adet , end="")

def kare(adet):
    print("#" * adet , end = "")
main()