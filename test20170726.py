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

lists = ['a*', 'abc', 'ab*', '*']

str = 'abc'

i = 0
j = 0
length = len(str)

for i in range(0, length):
    if i > 0 and i != length-1:
        str = str[:length-i] + '*'
    elif i == length-1:
        str = '*'

    for list in lists:
        if list == str:
            j = j + 1
        if j > 0:
            break
    if j > 0:
        break

if j == 0:
    print('Not found')
else:
    print(list)