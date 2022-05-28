users_input = input('Введите номер месяца\n')
users_number = int(users_input)


def season(month):
    if 1 <= month <= 2 or month == 12:
        print('Время года указанного месяца - зима')
    elif 2 < month <= 5:
        print('Время года указанного месяца - весна')
    elif 5 < month <= 8:
        print('Время года указанного месяца - лето')
    elif 9 < month <= 11:
        print('Время года указанного месяца - осень')
    else:
        print('Некорректное число. Пожалуйста, укажите число от 1 до 12')


season(users_number)
