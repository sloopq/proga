n = int(input("Введите натуральное число n: "))

# Вычисляем максимальное количество разрядов в числах
max_digits = len(str(n))

for i in range(1, n + 1):
    # Создаем строку, состоящую из чисел от 1 до i с выравниванием по правому краю
    stair = ''.join(str(j).rjust(max_digits) for j in range(1, i + 1))
    print(stair)