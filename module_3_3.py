def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(3, 2)
print_params(c = 25)
print_params(b = 35)
print_params(c = [1,2,3])

values_list = [3, 'Привет', False]
values_dict = {'a' : 5, 'b' : 'Привет', 'c' : True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['Как дела?', 555]
print_params(*values_list_2, 42)