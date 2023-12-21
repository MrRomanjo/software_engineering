def calc_x(z):
    x = z**2 + z**3
    return x


def calc_y(z):
    y = z + (z * 2)
    return y


def calc_f(x, y):
    return x + y


result = calc_f(calc_x(2), calc_y(3))     # x(2); y(3);
print(result)
