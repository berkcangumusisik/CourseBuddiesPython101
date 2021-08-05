""" Bir işçinin ilk maaşı (aylık) ve çalıştığı aylar verildiğinde kazandığı toplam parayı hesaplayan 
bir fonksiyon yazın. Her yıl işçi işte, maaşları ayda 100 dolar artıyor.

"""

def calculate_pay(initial_salary, months_worked):
    totalMoney = 0
    for i in range(1,months_worked+ 1):
        totalMoney += initial_salary 
        if i % 12 == 0 : initial_salary += 100
    return totalMoney

print(calculate_pay(1000,12))
print(calculate_pay(1000,20))