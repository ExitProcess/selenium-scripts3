class Fibo():
    a = 0
    b = 1

    def test(self):
        Fibo.a, Fibo.b = Fibo.b, Fibo.a + Fibo.b


f = Fibo()
print(f.a)

f.test()
print(f.a)

f.test()
print(f.a)

f.test()
print(f.a)
