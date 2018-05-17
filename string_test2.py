import time

start = time.time()

for str_count in range(1, 10000000):
    # локатор аптайма
    x = ["//tr[", str(str_count), "]/td[8]"]
    percents_xpath = "".join(x)
    print(percents_xpath)

print("%s seconds" % (time.time() - start))

# python -m dis string_test2.py
#
#   7          32 LOAD_CONST               4 ('//tr[')
#              34 LOAD_NAME                4 (str)
#              36 LOAD_NAME                3 (i)
#              38 CALL_FUNCTION            1
#              40 LOAD_CONST               5 (']/td[8]')
#              42 BUILD_LIST               3
#              44 STORE_NAME               5 (x)
#
#   8          46 LOAD_CONST               6 ('')
#              48 LOAD_ATTR                6 (join)
#              50 LOAD_NAME                5 (x)
#              52 CALL_FUNCTION            1
#              54 STORE_NAME               7 (percents_xpath)
#
# for i in range(1, 10000000):
# 63.08060812950134 seconds
#