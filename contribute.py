def add(*args):
    return sum(args)


def mul(*args):
    result = 1
    for num in args:
        result *= num
    return result


def sub(a, b):
    return abs(a-b)
