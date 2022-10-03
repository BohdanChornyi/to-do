def arithmetic(number1, number2, operation):
    result = 0
    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    elif operation == '/':
        result = number1 / number2
    else:
        result = "Unknow operation"
    return result
