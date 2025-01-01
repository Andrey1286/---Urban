def apply_all_func(int_list, *functions):
    list_int = []
    for i in int_list:
        if isinstance(i, (int, float)):
            list_int.append(i)
        else:
            list_int.append(len(i))
    results = {}
    for function in functions:
        results[function.__name__] = function(list_int)
    return results

print(apply_all_func([6, 'привет', 15, 9], max, min))

print(apply_all_func([6, 20, 15, 9], len, sum, sorted))