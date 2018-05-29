# в скрипте list_cmp_methods.py сравнивалась скорость 3 методов
# в этом скрипте проводится аналогичное сравнение с учетом реального применения метода, т.е. полученные вначале строки
# преобразованы в int, а потом полученный список сравнивается с отсортированным списком
# первые 2 метода остаются неизменными, только помимо простого сравнения <>, сравнивается еще и len() <>

import time

# создание списка из строк, строки вида $100000
x = 5000000
##############################################################################
list_inc1 = [("$" + str(i)) for i in range(0, x)]

time1 = time.time()
count = 0
for i in range(0, len(list_inc1) - 1):
    if list_inc1[i + 1] > list_inc1[i] or len(list_inc1[i + 1]) > len(list_inc1[i]):
        count += 1
if list_inc1[-1] > list_inc1[-2] or len(list_inc1[-1]) > len(list_inc1[-2]):
    count += 1
assert count == len(list_inc1)
print("элементов: ", count)
print("элементы расположены по возрастанию")
time1 = time.time() - time1
##############################################################################

##############################################################################
list_inc2 = [("$" + str(i)) for i in range(0, x)]

time2 = time.time()
count2 = 0
for i in range(0, len(list_inc2)):
    try:
        if list_inc2[i + 1] > list_inc2[i] or len(list_inc2[i + 1]) > len(list_inc2[i]):
            count2 += 1
    except Exception:
        if list_inc2[-1] > list_inc2[-2] or len(list_inc2[-1]) > len(list_inc2[-2]):
            count2 += 1
assert count2 == len(list_inc2)
print("элементов: ", count2)
print("элементы расположены по возрастанию")
time2 = time.time() - time2
##############################################################################

##############################################################################
list_inc3 = [("$" + str(i)) for i in range(0, x)]

time3 = time.time()
index = 0
for element in list_inc3:
    #   "$100" -->> 100
    list_inc3[index] = int(element[1:])
    index += 1

list_inc3_copy = list(list_inc3)
list_inc3_copy.sort()
assert list_inc3_copy == list_inc3
print("элементов: ", len(list_inc3))
print("элементы расположены по возрастанию")
time3 = time.time() - time3
##############################################################################

##############################################################################
list_inc4 = [("$" + str(i)) for i in range(0, x)]

time4 = time.time()
for (index, element) in enumerate(list_inc4):
    #   "$100" -->> 100
    list_inc4[index] = int(element[1:])

list_inc4_copy = list(list_inc4)
list_inc4_copy.sort()
assert list_inc4_copy == list_inc4
print("элементов: ", len(list_inc4))
print("элементы расположены по возрастанию")
time4 = time.time() - time4
##############################################################################

print("сравнение по очереди кроме последнего, последний вне цикла: ", time1)
print("сравнение по очереди в цикле через try / except: ", time2)
print("преобразование str -> int в цикле; копирование, list.sort и сравнение: ", time3)
print("преобразование str -> int через enumerate; копирование, затем list.sort и сравнение: ", time4)

# сравнение по очереди кроме последнего, последний вне цикла:  2.2121262550354004
# сравнение по очереди в цикле через try / except:  2.386136531829834
# преобразование str -> int в цикле; копирование, list.sort и сравнение:  3.6512091159820557
# преобразование str -> int через enumerate; копирование, затем list.sort и сравнение:  3.2681868076324463
