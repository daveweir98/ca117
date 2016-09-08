def power(n,m):
    if m == 1:
        return n
    if m == 0:
        return 1
    return n * power(n, m-1)
