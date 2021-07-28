"""İki sayı ve bir operatör (+, -, *, /) alan ve hesaplamanın sonucunu döndüren bir fonksiyon yazın."""

def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    
    elif operator == "*":
        return num1 * num2
    
    elif operator == "/":
        return num1 / num2
    
print(calculate(5,"+",7))
print(calculate(5,"-",7))
print(calculate(5,"*",7))
print(calculate(5,"/",7))