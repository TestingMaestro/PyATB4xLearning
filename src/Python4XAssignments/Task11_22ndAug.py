"""
Task #11 -
✅ Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13

"""
# Logic 1
a = 0
b = 1
num1 = int(input("Enter the number\n"))
for i in range(num1):
    print(a)
    a = a + b
    b = a - b

# Logic 2
num2 = int(input("Enter the number\n"))
m = 0
# n = 1
for j in range(num2):
    print(m)
    temp = m + n
    m = n
    n = temp
