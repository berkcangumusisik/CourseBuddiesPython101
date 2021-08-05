"""
Bir işçinin ilk maaşı (yıllık) ve çalıştığı yıl verildiğinde kazandığı toplam parayı hesaplayan 
bir fonksiyon yazın. İşçi işte olduğu her yıl maaşı 1000 dolar artıyor.
"""

def calculate_pay(initial_salary, years_worked):
    totalMoney = 0
    for i in range(years_worked):
        totalMoney += initial_salary
        initial_salary += 1000
    return totalMoney
print(calculate_pay(1000,5))