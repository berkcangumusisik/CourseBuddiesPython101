num = 0
tot = 0.0
while True:
    sval = input("Bir sayı giriniz:")
    if sval == "done":
        break
    try:
        fval = float(sval)
    except:
        print("Yanluş giriş yaptınız")
        continue
    num += 1
    tot += fval
print(tot,num,tot/num)