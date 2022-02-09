def dziadek(droga):

    droga = droga.upper()

    znaki = [' ', '-', '.', ',', ';']
    n = len(droga) - 1

    for i in droga:
        if i in znaki:
            droga = droga.replace(i, '')

    direction = 'up'
    tmp_digits = ''
    x = 0
    y = 0

    for i in droga:
        if i.isdigit():
            tmp_digits += i
        if (i == 'Z' or i == 'L' or i == 'P') or (len(droga) == 1):
            if direction == 'up':
                y = y + int(tmp_digits)
                tmp_digits = ''
            elif direction == 'down':
                y = y - int(tmp_digits)
                tmp_digits = ''
            elif direction == 'right':
                x = x + int(tmp_digits)
                tmp_digits = ''
            elif direction == 'left':
                x = x - int(tmp_digits)
                tmp_digits = ''

            if i == 'Z':
                if direction == 'up':
                    direction = 'down'
                elif direction == 'down':
                    direction = 'up'
                elif direction == 'right':
                    direction = 'left'
                elif direction == 'left':
                    direction = 'right'

            elif i == 'L':
                if direction == 'up':
                    direction = 'left'
                elif direction == 'down':
                    direction = 'right'
                elif direction == 'right':
                    direction = 'up'
                elif direction == 'left':
                    direction = 'down'

            elif i == 'P':
                if direction == 'up':
                    direction = 'right'
                elif direction == 'down':
                    direction = 'left'
                elif direction == 'right':
                    direction = 'down'
                elif direction == 'left':
                    direction = 'up'

        droga = list(droga)
        droga.pop()
        droga = ''.join(droga)

    if x == 0 and y == 0:
        return True
    else:
        return False


print(dziadek('20P20P20P20'))  # true
print(dziadek('20P20L20P20'))  # false
print(dziadek('20Z20'))  # true
print(dziadek('20Z10'))  # false
print(dziadek('100Z20P10Z10P80'))  # true
