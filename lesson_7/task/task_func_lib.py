def func_1_0(u):
    """bubble sort"""
    for i in range(1, len(u)):
        for j in range(len(u) - i):
            if u[j] > u[j + 1]:
                u[j], u[j + 1] = u[j + 1], u[j]


def func_1_1(u):
    """bubble sort improved"""
    for i in range(1, len(u)):
        e = True
        for j in range(len(u) - i):
            if u[j] > u[j + 1]:
                u[j], u[j + 1] = u[j + 1], u[j]
                e = False
        if e:
            break


def func_2(u):
    """selection sort"""
    for i in range(0, len(u)):
        k = i
        for j in range(k + 1, len(u)):
            if u[j] < u[k]:
                k = j
        u[i], u[k] = u[k], u[i]


def func_3(u):
    """insertion sort"""
    for i in range(1, len(u)):
        x = u[i]
        j = i
        while 0 < j and x < u[j - 1]:
            u[j] = u[j - 1]
            j -= 1
        u[j] = x
