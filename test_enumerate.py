# тест скорости обычного цикла против enumerate

import time

x = 10000000

###########################################################
elements1 = [("777" + str(i)) for i in range(0, x)]

for_in = time.time()

count = 0
for element in elements1:
    elements1[count] = int(element)
    count += 1

for_in = time.time() - for_in

print("обычный for in: ", for_in)
###########################################################

###########################################################
elements2 = [("777" + str(i)) for i in range(0, x)]

enum_time = time.time()

for (index2, element2) in enumerate(elements2):
    elements2[index2] = int(element2)

enum_time = time.time() - enum_time

print("enumerate: ", enum_time)
###########################################################

# x = 10000000
# обычный for in:  5.985342025756836
# enumerate:  5.213298320770264
