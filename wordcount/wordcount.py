
def wordcount(file_name: str):
    text_file = open(file_name, 'r')
    data: str = text_file.read()
    data = data.lower()
    # format string
    chars_to_delete = ['\n', '\t', '.', ',', ';', ':', '?', '!']
    for char in chars_to_delete:
        data = data.replace(char, ' ')
    data = data.split()
    word_count = {}
    # count occurences
    for word in data:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    # clean dictionary
    cleaned_dict = {}
    for word in word_count.keys():
        if word_count[word] >= 2 and len(word) > 2:
            cleaned_dict[word] = word_count[word]

    text_file.close()
    return cleaned_dict


print(wordcount('mruczanka.txt'))
