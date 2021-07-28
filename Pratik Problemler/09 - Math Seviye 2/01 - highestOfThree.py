"""Üç sayı alan ve en yüksek sayıyı döndüren bir fonksiyon yazın."""

def highest(num1, num2, num3):
    enBuyuk = num1
    if num2 > num1 and num2 > num3:
        enBuyuk= num2
        return num2
    elif num3 > num1 and num3 > num2:
        enBuyuk= num3
        return num3
    elif num1 > num2 and num1 > num3:
        enBuyuk= num1
        return num1


print(highest(5,12,13))