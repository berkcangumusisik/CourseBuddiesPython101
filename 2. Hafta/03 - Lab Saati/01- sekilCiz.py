def draw_shape(shape, count):
    hex=count
    if shape=="1":
        for i in range(count):
            print("* "*(i+1))
    elif shape=="2":
        for i in range(count):
            print(" "* count + ("*"*i)*2)
            count-=1
    elif shape=="3":
        for i in range(count):
            print("* "*5)
    elif shape=="4":
        col = int(input("sütun sayısını giriniz: "))
        for i in range(count):
            print("* "*col)
    elif shape=="5":
        for i in range(count):
            print(" "*hex+"* "*(count+i)+" "*hex)
            hex-=1
        for j in range(count,0,-1):
            print(" "*hex+"* "*(count+j)+" "*hex)
            hex+=1

print("1-dik üçgen\n2-eşkenar üçgen\n3-kare\n4-dikdörtgen\n5-altıgen\n")
draw_inp = input("hangi şekli çizmemi istiyorsun : ")
count_inp = int(input("satır sayısını giriniz : "))

draw_shape(draw_inp, count_inp)