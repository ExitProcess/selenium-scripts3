def fibo(n):
    a, b = 0, 1
    while n > 0:
        print(a)
        a, b = b, a+ b
        n -= 1


fibo(5555)
