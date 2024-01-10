#!/usr/bin/python3
""" Pascal's Traingle Module """


def pascal_triangle(n):
    """ returns a list of lists of integers
    representing the Pascal’s triangle of n """

    res = []
    if n <= 0:
        return res

    if n == 1:
        res.append([1])
        return res

    res = pascal_triangle(n - 1)
    focus = res[-1]
    size = len(focus)

    cur = []
    for i in range(size):
        if i == 0:
            cur.append(1)
        if i > 0 and i < size:
            cur.append((focus[i] + focus[i - 1]))
        if i == size - 1:
            cur.append(1)
    res.append(cur)

    return res
