""" 
Yol Gezisi Ortalama Hızı

Birkaç mil alan ve toplam yolculuğun ortalama hızını hesaplayan bir fonksiyon yazın. 
Aşağıdaki kuralları kullanın:

Bir yolculuğun ilk ve son 15 milinde 30 mph hız sınırı vardır
Yolculuğun ortasındaki hız sınırı 60 mph sınırına sahiptir.
"""


def average_speed(miles):
    if miles <= 30: return 30
    totalTime = ((miles-30)/60) + 1
    return miles /totalTime

print(average_speed(120))