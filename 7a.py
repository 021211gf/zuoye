def f(x):
    return x ** 3 - x - 1


a = 1.0
b = 1.5
while (b - a) > 0.001:
    c = (a + b) / 2
    if f(c) == 0:
        break
    elif f(a) * f(c) < 0:
        b = c
    else:
        a = c
print(f"方程的根约为: {round((a + b) / 2, 2)}")