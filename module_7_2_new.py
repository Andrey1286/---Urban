def custom_write(file_name, strings):
    counter = 0
    strings_positions = {}
    file = open(file_name, 'a', encoding='utf-8')
    for string in strings:
        counter += 1
        strings_positions[counter, file.tell()] = string
        file.write(f'{string}\n')
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
