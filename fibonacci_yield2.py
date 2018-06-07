def fibo(x):
    a, b = 0, 1
    while x > 0:
        yield a
        a, b = b, a + b
        x -= 1


for n in fibo(5555):
    print(n)
