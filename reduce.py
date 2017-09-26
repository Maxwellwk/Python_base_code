from functools import reduce
li = [10, 20, 30, 40, 50]

# reduce(函数， 对象)
ret = reduce(lambda x, y: x+y, li)

# print(ret)

ret = reduce(lambda x, y: x+y, li, 100)
print(ret)
