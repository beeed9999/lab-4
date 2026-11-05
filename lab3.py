
a = input("введите один символ: ")

if len(a) != 1:
    print('ошибка')
elif a.isdigit():
    print('данный символ это число')
elif a.isalpha():
    print('данный символ это буква')
else:
    print('это другой символ')
    