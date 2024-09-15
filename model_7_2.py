def custom_write(file_name, strings, o = 1):
    file = open(file_name, "a", encoding= "utf-8")
    strings_positions = {}
    for i in range(len(info)):
        strings_positions[o, file.tell()] = strings[o - 1]
        file.write(f'{strings[i]}\n')
        o = o + 1
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