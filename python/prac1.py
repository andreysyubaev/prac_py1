""" print("задание 1")
a = [1,1,2,3,5,8,10,12,34,38,40,41,46,50,55,89]
for i in a:
    if i < 15:
        print(i) """
        
""" print("задание 2")
a = int(input("Введите число: "))
if a < 0:
    print("число отрицательное")
elif a > 0:
    print("число положительное")
else:
    print("число равно нулю") """
    
""" print("задание 3")
x = str(input("выберите ( /  *  -  + ): "))
a = 15
b = 10
if x == '/':
    print(a / b)
elif x == '*':
    print(a * b)
elif x == '-':
    print(a - b)
elif x == '+':
    print(a + b)
else:
    print("error") """

""" print("задание 4")
a = 10
while a > 0:
    print(a)
    a = a - 1 """
    
print("задание 5")
import math
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Уравнение имеет два корня: {x1} и {x2}")
elif discriminant == 0:
    x = -b / (2*a)
    print(f"Уравнение имеет один корень: {x}")
else:
    print("Уравнение не имеет действительных корней")