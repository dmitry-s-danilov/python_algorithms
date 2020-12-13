from hashlib import sha1


def func_1(s, verbose=False):
    """Calculates a number of substring
using a set of substrings."""

    m = 1  # substring minimum length
    assert len(s) >= m + 1, \
        f'The string must contain more than {m} character(s).'
    n = len(s) - 1  # substring maximum length

    # Iterates over all substrings
    # adding each one to the set.

    v = set()  # a set of substrings
    for k in range(m, n + 1):
        for i in range(len(s) - k + 1):
            u = s[i: i + k]  # a substring
            if u not in v:
                v.add(u)

    if verbose:
        return v

    return len(v)


def func_2(s, verbose=False):
    """Calculates a number of substring
using a dict of occurrence frequencies of substrings."""

    m = 1  # substring minimum length
    assert len(s) >= m + 1, \
        f'The string must contain more than {m} character(s).'
    n = len(s) - 1  # substring maximum length

    # Iterates over all substrings
    # adding each one to the dict
    # or incrementing its frequency.

    v = dict()  # a dict of substrings
    for k in range(m, n + 1):
        for i in range(len(s) - k + 1):
            u = s[i: i + k]  # a substring
            if u not in v:
                v[u] = 1
            else:
                v[u] += 1

    if verbose:
        return v
    return len(v)


def func_3(s, verbose=False):
    """Calculates a number of substring
using a list of substring hashes."""

    m = 1  # substring minimum length
    assert len(s) >= m + 1, \
        f'The string must contain more than {m} character(s).'
    n = len(s) - 1  # substring maximum length

    # Iterates over all substrings
    # adding the hash of each one to the list.

    v = []  # a list of substrings hashes
    for k in range(m, n + 1):
        for i in range(len(s) - k + 1):
            u = sha1(
                s[i: i + k].encode('utf8')).hexdigest()  # a substring hash

            #             is_unique = True
            #             for _ in v:
            #                 if _ == u:
            #                     is_unique = False
            #                     break
            #             if is_unique:
            #                 v.append(u)

            if u not in v:
                v.append(u)

    if verbose:
        return v
    return len(v)
