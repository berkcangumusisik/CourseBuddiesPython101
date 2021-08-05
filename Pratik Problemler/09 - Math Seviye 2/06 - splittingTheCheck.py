"""
Bir yemeğin fiyatını ve akşam yemeğindeki kişi sayısını alacak ve her bir kişinin ödemesi gereken 
fiyatı hesaplayacak bir fonksiyon yazın. Toplama %20 bahşiş eklemeyi unutmayın!
"""

def split_check(price, num_people):
    kisiBasiOdeme = price / num_people
    bahsis = price * 0.2 / num_people
    kisiBasiOdeme += bahsis
    return kisiBasiOdeme

print(split_check(100, 4))
