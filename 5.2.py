while True:
    x = int(input('Введите число:'))
    if x == 0:
        break

    if x % 2 == 1:
        print('Плохо')
    elif 2 <= x <= 5 and x % 2 == 0:
        print('Неплохо')
    elif 6 <= x <= 20 and x % 2 == 0:
        print('так себе')
    elif x > 20 and x % 2 == 0:
        print('Отлично')
