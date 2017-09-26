li = [1, 2, 3, 4, 5]

# map (函数， 处理对象)
# 返回可迭代对象

# def fun(x):
#     return x+1
# ret = map(fun, li)
# print(list(ret))
# ret = map(lambda x : x + 1, li)
# print(list(ret))

li1 = [1, 2, 3, 4]
li2 = [5, 6, 7, 8]
ret = map(lambda x, y: x + y, li1, li2)
print(list(ret))





