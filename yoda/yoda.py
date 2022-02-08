def yoda_translator(file_name: str) -> None:
    text_file = open(file_name, 'r')
    # extract to one string
    data: str = text_file.read()
    data = data.lower()
    # divide into sentences
    sentence_list = data.split('.')
    if len(sentence_list[-1]) == 0:
        sentence_list.pop()
    new_sentence_list = []
    # reverse sentences
    for sentence in sentence_list:
        sentence = sentence.split(' ')
        if len(sentence[0]) == 0:
            sentence.pop(0)
        sentence.reverse()
        sentence[0] = sentence[0].capitalize()
        sentence = ' '.join(sentence) + '.'
        new_sentence_list.append(sentence)
    # join new sentences
    new_data = ' '.join(new_sentence_list)
    # print(new_data)
    text_file.close()
    output_file_name = file_name.split('.')[0] + '.yda'
    # print(output_file_name)
    # write new sentences into the file
    text_file = open(output_file_name, 'w')
    text_file.write(new_data)
    text_file.close()


yoda_translator('kubuspuchatek.txt')
