# def sum_three_num(a,b,c)
# return a + b + c

any = lambda a, b, c: a + b + c
print(any(10, 20, 100))

# even-odd
num = 2
if num % 2 == 0:
    print("even")
else:
    print("odd")

# Lambda Expression
res = lambda num: "even" if num % 2 == 0 else "odd"
print(res(num))
