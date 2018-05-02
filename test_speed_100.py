# скажем, надо проверить условие, содержит ли строка подстроку "100"
# есть такие методы:
# S.find("100")
# S.index("100") (с исключениями)
# if "100" in S
# if S[0:3] == "100"
# более быстрый из них -- это if "100" in S, но надо проверить

import time

elements = ["100% (70000000000000000000000000000000000000) +" for i in range(1, 9000000)]

if_in = time.time()
count = 0
for element in elements:
    if "100" in element:
        count += 1
if_in = time.time() - if_in

print("if in найдено: ", count)
print("времени затрачено: ", if_in)


s_find = time.time()
count = 0
for element in elements:
    element.find("100")
    if True:
        count += 1
s_find = time.time() - s_find

print("s.find найдено: ", count)
print("времени затрачено: ", s_find)


s_index = time.time()
count = 0
for element in elements:
    element.index("100")
    if True:
        count += 1
s_index = time.time() - s_index

print("s.index найдено: ", count)
print("времени затрачено: ", s_index)


if_equ = time.time()
count = 0
for element in elements:
    if element[0:3] == "100":
        count += 1
if_equ = time.time() - if_equ

print("if equ найдено: ", count)
print("времени затрачено: ", if_equ)


and_true = time.time()
count = 0
for element in elements:
    if element[0:3] and "100":
        count += 1
and_true = time.time() - and_true

print("and ... true: ", count)
print("времени затрачено: ", and_true)
