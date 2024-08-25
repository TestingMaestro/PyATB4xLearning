m = 100
n = 200
p = 300


def sum_of_three(a, b, c=100):
    return a + b + c


# res = sum_of_three(a=1, b=1, c=20)
# print(res)
# res = sum_of_three(20, 10, 90)
# print(res)
# res = sum_of_three(a=m, b=n, c=p)
# print(res)

# res = sum_of_three(a=100)
# print(res)
res = sum_of_three(a=100, b=200)
print("sum_of_three",res)


def sum_of_three_nos(m=10, n=20, p=100):
    return m + n + p


res = sum_of_three_nos()
print(res)
res = sum_of_three_nos(n=200)
print(res)
res = sum_of_three_nos(m=100,p=1000)
print(res)
res = sum_of_three_nos(100,400,2000)
print(res)
res = sum_of_three_nos(20,30)
print(res)

