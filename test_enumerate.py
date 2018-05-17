# тест скорости обычного цикла против enumerate

import time

elements = ["100% (70000000000000000000000000000000000000) +" for i in range(0, 100000000)]

for_in = time.time()
count = 0
for element in elements:
    if "100" in element:
        count += 1
for_in = time.time() - for_in

print("элементов в списке: ", count)
print("времени затрачено: ", for_in)

enum_time = time.time()

for (index, element) in enumerate(elements):
    if "100" in element:
        index += 1
enum_time = time.time() - enum_time

print("элементов в списке: ", index)
print("enumerate времени затрачено: ", enum_time)

# элементов в списке:  100000000
# времени затрачено:  24.672932624816895
# элементов в списке:  100000000
# enumerate времени затрачено:  35.64703869819641
