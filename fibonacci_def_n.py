def fibo(n):
    global b
    a, b = 0, 1
    # > 2 для ряда начинающегося с 0, > 1 для ряда начинающегося с 1
    while n > 1:
        a, b = b, a + b
        n -= 1
    return b


user = -1
while user != 0:
    user = input("n: ")
    user = int(user)
    fibo(user)
    print(b)
