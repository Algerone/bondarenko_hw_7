user_input = input('Введите длинну стороны\n')  # получаем число для вычислений
user_data = int(user_input)  # переводим значение из str в int


def square(side):  # функция в которой проводятся вычесления и указана функция для вывода результатов
    perimeter = side * 4
    diagonal = side * 0.707
    area = side ** 2
    print(f'Периметр = {perimeter}\nДиагональ = {round(diagonal, 3)}\nПлощадь = {area}')


square(user_data)  # указываем, что переменная side будет принимать значение из user_data
