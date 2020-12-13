def f(x):
    y = dict()
    z = 0
    for _ in x:
        y[_] = sum(x[_])
        z += y[_]

    z /= len(y)

    u, v = [], []
    for _ in y:
        if y[_] < z:
            u.append(_)
        elif y[_] > z:
            v.append(_)

    return z, u, v
