def add_everything_up(a, b):
    try:
        x = a + b
        if isinstance(x, float):
            x = round(x, 3)
        return x

    except TypeError as exc:
        return str(a) + str(b) + '(ошибка)'

    except ValueError as exc_2:
        return f'Невозможно преобразовать строку во флоат'

    # else:
    #     print('Всё получилось!')
    #
    # finally:
    #     print('Мы справились!')

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
