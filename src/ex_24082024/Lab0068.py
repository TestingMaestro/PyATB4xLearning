def sum_three(a=1, b=1, c=1):
    return a + b + c


res = sum_three()
print(res)  # 3
res = sum_three(1, 2)
print(res)
res = sum_three(1, 2, 3)
print(res)

res = sum_three(b=67, a=10, c=45)
print(res)
