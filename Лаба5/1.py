import math


def x(z):
    return (z * z) + 3


def y():
    return math.sin(4)


def f(x, y):
    return x + y


result = f(x(2), y())
print(result)
