#Ввод чисел
import math

a = float(input("введите a: "))
b = float(input("введите b: "))
c = float(input("введите c: "))

#определение уравнение и дискриминанта
if a == 0:
    print("неквадратное уравнение")
else:
    d = b**2 - 4*a*c
    
    #определение корней
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print(f"два корня: x1 = {x1:.2f}, x2 = {x2:.2f}")
    elif d == 0:
        x1 = -b / (2*a)
        print(f"один корень: {x1:.2f}")
    else:
        print(f"нет корней")