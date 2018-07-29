# There should be one — and preferably only one — obvious way to do it.
# Должен существовать один — и, желательно, только один — очевидный способ сделать это.

import time
import keyword

str_count = 5000000
str_list = ["any text" for i in range(0, str_count)]

####################################
print(len(str_list))
result = keyword.iskeyword("string")
print(result)
####################################

time1 = time.time()
f1 = open("1.txt", "w+")
for string in str_list:
    f1.write(string + "\n")
f1.close()
time1 = time.time() - time1

time2 = time.time()
f2 = open("2.txt", "w+")
for string in str_list:
    f2.write("%s\n" % string)
f2.close()
time2 = time.time() - time2

time3 = time.time()
f3 = open("3.txt", "w+")
for string in str_list:
    f3.write("{}{}".format(string, "\n"))
f3.close()
time3 = time.time() - time3

print(r'(string + "\n")', time1)
print(r'("%s\n" % string)', time2)
print(r'("{}{}".format(string, "\n"))', time3)

# 5000000
# False
# (string + "\n") 11.106635332107544
# ("%s\n" % string) 12.219698905944824
# ("{}{}".format(string, "\n")) 13.427767992019653
