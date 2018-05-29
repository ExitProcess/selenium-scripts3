# переместить 1 элемент списка в конец списка
# сравнение скорости 2-х методов:
#
# 1 метод -- list.append(list.pop(0))
#
# 2 метод -- list.append(list[0])
#            del list[0]
#

import time

x = 10
iter_count = 10000000

time1 = time.time()

for n in range(0, iter_count):
    list_inc1 = [i for i in range(0, x)]
    list_inc1.append(list_inc1.pop(0))
time1 = time.time() - time1

time2 = time.time()

for n in range(0, iter_count):
    list_inc2 = [i for i in range(0, x)]
    list_inc2.append(list_inc2[0])
    del list_inc2[0]
time2 = time.time() - time2

print("времени затрачено: ", time1)
print("времени затрачено: ", time2)

# x = 10
# iter_count = 70000000
# времени затрачено:  98.95565986633301
# времени затрачено:  89.06309413909912

# x = 10
# iter_count = 10000000
# времени затрачено:  14.068804740905762
# времени затрачено:  12.704726457595825

#########################################################
# python -m dis test_list_first_to_end.py
#
# 18          60 LOAD_NAME                6 (list_inc1)
#             62 LOAD_ATTR                7 (append)
#             64 LOAD_NAME                6 (list_inc1)
#             66 LOAD_ATTR                8 (pop)
#             68 LOAD_CONST               0 (0)
#             70 CALL_FUNCTION            1
#             72 CALL_FUNCTION            1
#             74 POP_TOP
#########################################################

#########################################################
# 26         136 LOAD_NAME               10 (list_inc2)
#            138 LOAD_ATTR                7 (append)
#            140 LOAD_NAME               10 (list_inc2)
#            142 LOAD_CONST               0 (0)
#            144 BINARY_SUBSCR
#            146 CALL_FUNCTION            1
#            148 POP_TOP
#
# 27         150 LOAD_NAME               10 (list_inc2)
#            152 LOAD_CONST               0 (0)
#            154 DELETE_SUBSCR
#########################################################
