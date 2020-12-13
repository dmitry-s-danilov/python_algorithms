calc_0 = lambda n: n * (n - 1) / 2


def func_1(n):
    """Returns handshake graph in adjacency matrix form."""

    g = [[1 if j != i else 0
          for j in range(n)]
         for i in range(n)]
    return g


def calc_1(g):
    """Calculates handshakes using graph in adjacency matrix form."""

    k = 0
    for i in range(len(g)):
        for j in range(i, len(g)):
            k += g[i][j]
    return k


def func_2(n):
    """Returns handshake graph in adjacency list form."""

    g = {i: {j for j in range(n)
             if j != i}
         for i in range(n)}
    return g


def calc_2(g):
    """Calculates handshake graph in adjacency list form."""

    k = 0
    h = set()
    for i in g:
        h.add(i)
        k += len(g[i].difference(h))
    return k


def func_3(n):
    """Returns handshake graph in edge list form."""

    g = {(i, j)
         for i in range(n)
         for j in range(n)
         if j != i}
    return g


def calc_3(g):
    """Calculates handshakes using graph in edge list form."""

    k = 0
    h = set()
    for _ in g:
        if _ not in h:
            k += 1
        h = h.union({_, _[::-1]})
    return k
