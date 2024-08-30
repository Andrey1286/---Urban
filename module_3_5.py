def get_multiplied_digits(number):
    str_number = str(number)
    first = int(list(str_number)[0])
    if int(str_number) < 10:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(2)
print(result)
