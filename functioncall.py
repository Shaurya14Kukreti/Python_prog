def add(x):
    return x + 1

def sub(x):
    return x - 1

def operat(func, x):
    result = func(x)
    print(result)
    return result


operat(add,5)
operat(sub,6)
