#Ввод чисел
a = float(input("введите первое число: "))
b = float(input("введите второе число: "))
c = float(input("введите третье число: "))
#узнать максимум
if a >= b and a >= c:
    maximum = a
elif b >= a and b >= c:
    maximum = b
else:
    maximum = c
print(f"максимум: {maximum}")