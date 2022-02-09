def is_pangram(input: str):
    input = input.lower()
    alphabet = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's', 'ś', 't', 'u', 'w', 'y', 'z', 'ź', 'ż']
    occurences = {}
    for letter in alphabet:
        occurences[letter] = 0
    # count occurences in input string
    for letter in input:
        if letter in alphabet:
            occurences[letter] += 1
            if occurences[letter] > 1:
                return None  # more than once

    missing_letters = []
    for key in occurences.keys():
        if occurences[key] != 1:
            missing_letters.append(key)

    return missing_letters


print(is_pangram('Dość gróźb fuzją, klnę, pych i małżeństw'))  # []
print(is_pangram('Ość gróźb fuzją, klnę, pych i małżeństw'))  # ['d']
print(is_pangram('oOść gróźb fuzją, klnę, pych i małżeństw'))  # None
