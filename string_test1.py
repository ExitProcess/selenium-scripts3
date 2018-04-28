import time

start_time = time.time()

for str_count in range(1, 1000000):
    # локатор аптайма
    percents_xpath = "//tr[" + str(str_count) + "]/td[8]"
    print(percents_xpath)

print("%s seconds" % (time.time() - start_time))

# python -m dis string_test1.py
#
#    7        32 LOAD_CONST               4 ('//tr[')
#             34 LOAD_NAME                4 (str)
#             36 LOAD_NAME                3 (str_count)
#             38 CALL_FUNCTION            1
#             40 BINARY_ADD
#             42 LOAD_CONST               5 (']/td[8]')
#             44 BINARY_ADD
#             46 STORE_NAME               5 (percents_xpath)
#
