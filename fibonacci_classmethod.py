class Fibo:
    a = 0
    b = 1

    @classmethod
    def fibo_change(cls, n):
        while n > 0:
            cls.a, cls.b = cls.b, cls.a + cls.b
            n -= 1


# создание экземпляра f класса Fibo (объекта f)
f = Fibo()
print(f.a, f.b)

# создание экземпляра f2 класса Fibo (объекта f2)
f2 = Fibo()
print(f2.a, f2.b)

# метод класса изменяет атрибуты класса, а не атрибуты экземпляра
f.fibo_change(10)
print(f.a, f.b)

print(f2.a, f2.b)

f3 = Fibo()
print(f3.a, f3.b)
