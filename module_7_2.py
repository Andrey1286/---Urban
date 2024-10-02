def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}

    for i, string in enumerate(strings, 1):
        row_position = file.tell()
        file.write(f'{string}\n')
        strings_positions[(i, row_position)] = string
    file.close()
    return strings_positions


info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)