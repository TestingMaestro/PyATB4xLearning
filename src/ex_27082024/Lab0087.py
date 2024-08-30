def add_10(m):
    return m + 10


res = add_10(10)
print(res)

# lambda expression

n = lambda m: m + 10
print(n(10))


def mul(x, y):
    return x * y


res1 = lambda x, y: x * y
print(res1(10, 20))
