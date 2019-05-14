def fib(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = a + b, a
    return a


def fibi(n):
    if n < 2: return n
    c = 1
    p = 0
    while n > 1:
        c, p = c + p, c
        n -= 1
    return c


print(fib(40))
