str = "1 Germany 1533(1532.68) 1609 0 784.89 784.89 804.19 402.09 463.51 139.05 1033.19 206.64"

# list = str.split(" ")
# print(list[0], list[1], list[2])

i = str.rfind(")")
print(str[0:i+1])
