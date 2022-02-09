def encrypt_sc(input: str, key: int) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = list(alphabet)

    input = input.lower()
    result = []
    for letter in input:
        if letter in alphabet:
            index = alphabet.index(letter)
            index += key
            if index < 0:
                index += len(alphabet)
            elif index > len(alphabet):
                index -= len(alphabet)
            result.append(alphabet[index])
            continue
        result.append(' ')
    result = ''.join(result).upper()
    return result


print(encrypt_sc('PRZECIWNIK CHOWA SIE W ZAGAJNIKU', 3))
