def jalukalk(input: str) -> float:
    input = list(input.replace(" ", ""))
    input.reverse()
    stack = []
    operations = ['+', '-', '/', '*']
    for argument in input:
        if argument.isdigit():
            stack.append(argument)
        elif argument in operations:
            try:
                a = stack.pop()
                b = stack.pop()
                stack.append(eval(f'{a}{argument}{b}'))
            except:
                return 'ERROR'
        else:
            return 'ERROR'

    return stack[0]


print(jalukalk('/ 7 + 2 3'))
