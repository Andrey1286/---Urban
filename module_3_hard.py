def calculate_structure_sum(data):
    total_amount = 0
    if isinstance(data, int):
        return data
    if isinstance(data, str):
        return len(data)
    for i in data:
        if isinstance(i, int):
            total_amount += i
        elif isinstance(i, str):
            total_amount += len(i)
        elif isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            total_amount += calculate_structure_sum(i)
        elif isinstance(i, dict):
            for key, value in i.items():
                total_amount += calculate_structure_sum(key)
                total_amount += calculate_structure_sum(value)
    return total_amount

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)