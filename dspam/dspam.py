def dspam_confidence(file_name: str) -> float:
    values = []
    text_file = open(file_name, 'r')
    data = text_file.read()
    chars_to_delete = ['\n', '\t', ',', ]
    for char in chars_to_delete:
        data = data.replace(char, ' ')
    data = data.split()
    i: int = 0
    # find values
    while i < len(data):
        if data[i] == 'X-DSPAM-Confidence:':
            values.append(float(data[i + 1]))
        i += 1
    # parse values (opt. round up to 6)
    average = round((sum(values) / len(values)), 6)
    text_file.close()
    return average


print(dspam_confidence('mejle.txt'))
