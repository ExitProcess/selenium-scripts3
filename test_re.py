import time
import re

elements = ["\n1\n" for i in range(0, 100000)]

time1 = time.time()

for element in elements:
    element2 = element[1:-1]
    print(element2)
time1 = time.time() - time1

time2 = time.time()
for element in elements:
    element2 = re.findall('(\d+)', element)
    print(element2[0])
time2 = time.time() - time2


print("времени затрачено: ", time1)
print("времени затрачено: ", time2)