li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filter 过滤器
# filte(函数， 对象)

def fun(x):
    # 如果保留这个元素， 返回TRUE
    # 如果丢弃这个元素， 返回FALSE
    if x%2 == 0:
        return  True
    else:
        return False
# ret = filter(fun, li)
ret = filter(lambda x : x%2==0, li)

print(list(ret))

