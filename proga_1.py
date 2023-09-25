def count_matching_numbers(a, b, c):
    if a == b == c:
        return 3
    elif a == b or a == c or b == c:
        return 2
    else:
        return 0

# Ввод трех чисел с клавиатуры
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

# Вызываем функцию и выводим результат
result = count_matching_numbers(num1, num2, num3)
print("Результат:", result)