import math


def x():
    return (math.cos(5))**2


def y(z):
    return (z * z * z) - 1


def f(x, y):
    return x + y


result = f(x(), y(3))
print(result)
