# 斐波那契数列的计算
# 主要是熟悉递归定义
# 注意参数值为37的时候已经要计算十几秒了，再大了就不知道要计算多久了
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(37))