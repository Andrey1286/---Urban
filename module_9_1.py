def apply_all_func(int_list: list, *functions):
    results_list = []
    list_of_functions = []
    results = {}
    for i in functions:
        x = i.__name__
        results_list.append(i(int_list))
        list_of_functions.append(x)
    for key, value in zip(list_of_functions, results_list):
        results[key] = value
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))