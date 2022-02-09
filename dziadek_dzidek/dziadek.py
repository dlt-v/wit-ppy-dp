def dziadekDzidek(plan: str) -> bool:
    coords = [0, 0]  # y, x
    is_y: bool = True
    forward_y: bool = True
    forward_x: bool = True

    i: int = 0

    while i < len(plan):
        symb: str = plan[i]
        if symb == 'Z':  # inverse
            if is_y:
                forward_y = not forward_y
            else:
                forward_x = not forward_x

            i += 1

        elif symb == 'L':  # turn left
            if is_y:
                forward_x = not forward_y
            else:
                forward_y = forward_x

            is_y = not is_y
            i += 1

        elif symb == 'P':  # turn right
            if is_y:
                forward_x = forward_y
            else:
                forward_y = not forward_x
            is_y = not is_y
            i += 1

        elif symb.isdigit():
            step_length: str = symb

            while True:
                if i + 1 == len(plan):
                    i += 1
                    break
                elif plan[i + 1].isdigit():
                    i += 1
                    step_length += plan[i]
                else:
                    i += 1
                    break

            if is_y:
                if forward_y:
                    coords[0] += int(step_length)
                else:
                    coords[0] -= int(step_length)
            else:
                if forward_x:
                    coords[1] += int(step_length)
                else:
                    coords[1] -= int(step_length)
        else:
            i += 1

    if sum(coords) == 0:
        return True
    else:
        return False


print(dziadekDzidek('20P20P20P20'))  # -> True
print(dziadekDzidek('20P20L20P20'))  # -> False
print(dziadekDzidek('20Z20'))  # -> True
print(dziadekDzidek('20Z10'))  # -> False
print(dziadekDzidek('100Z20P10Z10P80'))  # -> True
