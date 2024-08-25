"""

Task #10 -
✅ Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24

Task #11 -
✅ Fibonacci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13

"""

# Factorial

num = int(input("Enter the number\n"))


def factorial_num(n, fact=1):
    for i in range(n, 0, -1):
        fact = fact * i
    print(f"{n}! =", fact)


def fibonacci_series(n, a=0, b=1, temp=0):
    print("Fibonacci series are:")
    for i in range(num):
        print(f"{a}", end=" ")
        temp = a + b
        a = b
        b = temp
    print("\n")
    factorial_num(n=num)


fibonacci_series(n=num)
