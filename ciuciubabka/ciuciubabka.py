def ciuciubabka(file_name):
    text_file = open(file_name, 'r', encoding='utf-8')
    data = text_file.read()
    data = data.replace('\n', ' ')
    data = data.split()
    coords = [0, 0]  # x, y
    i = 0
    while i < len(data):
        if data[i] == 'przód':
            coords[1] += int(data[i+1])
        elif data[i] == 'tył':
            coords[1] -= int(data[i+1])
        elif data[i] == 'lewo':
            coords[0] -= int(data[i+1])
        elif data[i] == 'prawo':
            coords[0] += int(data[i+1])
        i += 2
    return round(abs(0 - coords[0]) + abs(0 - coords[1]))


print(ciuciubabka('polecenia.txt'))
