first_list: list = [1, 2, 3, 4]
second_list: list = [11, 22, 33, 44]
concat_list = []


def concat(x, y):
    for i in range(0, len(x)):
        concat_list.append(x[i])
        concat_list.append(y[i])
    print(concat_list)


concat(first_list, second_list)
