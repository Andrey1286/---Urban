
def calculate_structure_sum(*arg):
    list_of_numbers = []
    x = 0
    for i in arg:
        if isinstance(i, str):
            list_of_numbers.append(stroka)
        elif isinstance(i, list):
            for j in i:
                if isinstance(j, int):
                    list_of_numbers.append(j)
                elif isinstance(j, str):
                    list_of_numbers.append(stroka)
                elif isinstance(i, dict):
                    number1 = list(zip(i))
                    for k in number1:
                        if isinstance(k, str):
                            list_of_numbers.append(stroka)
                        elif isinstance(k, int):
                            list_of_numbers.append(k)
        elif isinstance(i, dict):
            number2 = list(zip(i))
            for f in number2:
                if isinstance(f, str):
                    list_of_numbers.append(stroka)
                if isinstance(f, int):
                    list_of_numbers.append(f)
        if x == 0:
            print(list_of_numbers)
            exit()
        x += 1

    return sum(list_of_numbers)

data_structure = [
        [1, 2, 3],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])]

stroka = 1

result = calculate_structure_sum(data_structure)
print(result)