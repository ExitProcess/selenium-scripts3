a, b = 0, 1


def fibo():
    global a
    global b
    a, b = b, a + b
    print(a)


fibo()
fibo()
fibo()
fibo()
fibo()
fibo()
fibo()
