# import random
#
# def ran(count,num=1):
#
#     str = '3460'
#     a = []
#     n = num
#     for i in range(0, count):
#         for j in range(0, n):
#             if num > 0:
#                 a.append(random.choice(str))
#                 num = num - 1
#             else:
#                 print(a)
#                 a = []
#                 num = n
# ran(20,8)

from common.myFile import myFile

txt = myFile('./txt.txt')

for i in range(1,501):
    str = '"k%s":"v%s",' % (i, i)
    # print(str)
    txt.write(str)