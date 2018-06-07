def fibo(x):
    a, b = 0, 1
    while a < x:
        yield a
        a, b = b, a + b


for n in fibo(100000):
    print(n)
