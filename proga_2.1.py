n = int(input("Введите натуральное число n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()


n = int(input("Введите натуральное число n: "))

for i in range(1, n + 1):
    # Создаем строку, состоящую из чисел от 1 до i
    stair = ''.join(str(j) for j in range(1, i + 1))
    print(stair)