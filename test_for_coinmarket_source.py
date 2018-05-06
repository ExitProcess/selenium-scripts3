import time

elements = ["\n\nXRP\nRiple\n" for i in range(0, 30000000)]

time1 = time.time()

count = 0
for element in elements:
    element = element[2:-1]
    count += 1

time1 = time.time() - time1
print("элементов: ", count)
print("времени затрачено: ", time1)

time2 = time.time()

count = 0
for element in elements:
    element = element.strip("\n")
    count += 1

time2 = time.time() - time2
print("элементов: ", count)
print("времени затрачено: ", time2)

# strip - 13.11680006980896
# срез -- 10.01495099067688