def funcion(a, b):
    if not((isinstance(a, int) & isinstance(b, int))):
        return -1
    if (a < b):
        return -2
    else:
        return (a+b, a*b, a-b)
