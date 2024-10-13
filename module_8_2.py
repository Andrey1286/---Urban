def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    for i in numbers:
        try:
            result += i
        except TypeError as exc:
            incorrect_data += 1
            if isinstance(i, str):
                print(f'Некорректный тип данных для подсчёта суммы - {i}')
            else:
                print(f'Некорректный тип данных для подсчёта суммы - {incorrect_data}')
    return result, incorrect_data

def calculate_average(numbers):
    try:
        total_sum, incorrect_data = personal_sum(numbers)
        all_numbers = len(numbers) - incorrect_data
        return total_sum / all_numbers
    except ZeroDivisionError as exc:
        return 0
    except TypeError as exc_2:
        print(f'В numbers записан некорректный тип данных')


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать