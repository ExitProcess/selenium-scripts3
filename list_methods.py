import time

x = 20000000
list_inc1 = [i for i in range(0, x)]

time1 = time.time()

count = 0
for i in range(0, len(list_inc1) - 1):
    if list_inc1[i + 1] > list_inc1[i]:
        count += 1
if list_inc1[-1] > list_inc1[-2]:
    count += 1
assert count == len(list_inc1)
print("элементов: ", count)
print("элементы расположены по возрастанию")

time1 = time.time() - time1


list_inc2 = [i for i in range(0, x)]

time2 = time.time()

count2 = 0
for i in range(0, len(list_inc2)):
    try:
        if list_inc2[i + 1] > list_inc2[i]:
            count2 += 1
    except Exception:
        if list_inc2[-1] > list_inc2[-2]:
            count2 += 1
assert count2 == len(list_inc2)
print("элементов: ", count2)
print("элементы расположены по возрастанию")

time2 = time.time() - time2


list_inc3 = [i for i in range(0, x)]

time3 = time.time()

list_inc_temp = list(list_inc3)
list_inc_temp.sort()
assert list_inc_temp == list_inc3
print("элементов: ", len(list_inc3))
print("элементы расположены по возрастанию")

time3 = time.time() - time3

print("времени затрачено: ", time1)
print("времени затрачено: ", time2)
print("времени затрачено: ", time3)

# элементов:  20000000
# элементы расположены по возрастанию
# элементов:  20000000
# элементы расположены по возрастанию
# элементов:  20000000
# элементы расположены по возрастанию
# времени затрачено:  8.86450719833374
# времени затрачено:  9.262529850006104
# времени затрачено:  0.5350308418273926
