def babagra(input: str) -> bool:
    input = input.lower()
    i: int = 0
    bzi_happaned: bool = False
    flag_um: bool = False
    while i < len(input):
        if i + 2 < len(input) and input[i] + input[i + 1] + input[i + 2] == 'bzi':
            bzi_happaned = not bzi_happaned
            i += 3
            continue

        elif bzi_happaned and input[i] != 'u':
            break
        elif i + 1 < len(input) and bzi_happaned and input[i] + input[i + 1] == 'um':
            flag_um = not flag_um
            break
        i += 1

    return flag_um


print(babagra('Kto znalazł bziuuuum ogon?'))
print(babagra('Ja - rzekł Puchatek.'))
print(babagra('Garnek śliczny był, nowiutki i bzium,'))
print(babagra('Bziuoam jak to milo Chmurka być...'))
print(babagra('bziuuuoum'))