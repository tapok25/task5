while True:
    x = int(input('Введите число от 1 до 9:'))
    if x == 0:
        break

    for i in range(x+1):
        if i == 0:
            continue
        print(i, end='')
    print()