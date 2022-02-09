def big_litera(letter: str, symbol: str):
    letters = {
        'A': [' *** ', '*   *', '*****', '*   *', '*   *'],
        'B': ['**** ', '*   *', '**** ', '*   *', '**** '],
        'C': [' ****', '*    ', '*    ', '*    ', ' ****'],
        'D': ['**** ', '*   *', '*   *', '*   *', '**** '],
        'E': ['*****', '*    ', '*****', '*    ', '*****'],
        'F': ['*****', '*    ', '***  ', '*    ', '*    '],
        'G': [' ****', '*    ', '*  **', '*   *', ' ****'],
        'H': ['*   *', '*   *', '*****', '*   *', '*   *'],
        'I': ['*****', '  *  ', '  *  ', '  *  ', '*****'],
        'J': ['*****', '    *', '    *', '*   *', ' *** '],
        'K': ['*   *', '*  * ', '**   ', '*  * ', '*   *'],
        'L': ['*    ', '*    ', '*    ', '*    ', '*****'],
        'M': ['*   *', '** **', '* * *', '*   *', '*   *'],
        'N': ['*   *', '**  *', '* * *', '*  **', '*   *'],
        'O': [' *** ', '*   *', '*   *', '*   *', ' *** '],
        'P': ['**** ', '*   *', '**** ', '*    ', '*    '],
        'Q': [' *** ', '*   *', '*   *', '*  **', ' ** *'],
        'R': ['**** ', '*   *', '**** ', '*  * ', '*   *'],
        'S': [' ****', '*    ', '**** ', '    *', '**** '],
        'T': ['*****', '  *  ', '  *  ', '  *  ', '  *  '],
        'U': ['*   *', '*   *', '*   *', '*   *', ' *** '],
        'V': ['*   *', '*   *', '*   *', ' * * ', '  *  '],
        'W': ['*   *', '*   *', '* * *', '** **', '*   *'],
        'X': ['*   *', ' * * ', '  *  ', ' * * ', '*   *'],
        # chuj w dupe kowalskiemu
        'Y': ['*   *', ' * * ', '  *  ', '  *  ', '  *  '],
        'Z': ['*****', '   * ', '  *  ', ' *   ', '*****'],
    }
    result = letters[letter.upper()]

    if symbol != '*':
        i = 0
        while i < 5:
            result[i] = result[i].replace('*', symbol)
            i += 1

    return result


result = big_litera('A', '^')
for line in result:
    print(line)
