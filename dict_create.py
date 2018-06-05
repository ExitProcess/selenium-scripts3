dict1 = {}
print(dict1)
dict1 = {'a': 1, 'b': 2}
print(dict1)

dict2 = dict(c=3, d=4)
print(dict2)

dict3 = dict.fromkeys(['e', 'f'], 5)
print(dict3)

dict4 = {x: x << 1 for x in range(0, 10)}  # x *= 2
print(dict4)
