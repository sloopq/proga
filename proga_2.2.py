n = int(input("Введите натуральное число n: "))

# Вычисляем ширину пирамиды, это будет длина последней строки
width = 2 * n - 1

for i in range(1, n + 1):
    # Создаем строку для текущей ступеньки
    stair = ''.join(str(j) for j in range(1, i + 1))
    # Добавляем обратную последовательность чисел, исключая 1
    stair += ''.join(str(j) for j in range(i - 1, 0, -1))
    # Выравниваем строку по центру и выводим
    print(stair.center(width))