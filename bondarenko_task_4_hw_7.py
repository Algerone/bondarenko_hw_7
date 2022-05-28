users_str = input('Введите слово\n')

def polyndrome(x):
    if x == x[::-1]:
        print(True)
    else:
        print(False)


polyndrome(users_str)