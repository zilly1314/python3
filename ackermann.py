def ack(m, n):
    """Ackermann函数，当数值较大时就出错了"""
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))
    # return 125
print(ack(3, 6))