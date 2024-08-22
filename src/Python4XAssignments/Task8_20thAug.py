### Task #9

# ✅ FizzBuzz Test:
#
# Write a program that prints numbers from 1 to 100. # Loop For
# However, for multiples of 3, print "Fizz" instead of the number, and
# for multiples of 5, print "Buzz."
# For numbers that are multiples of both 3 and 5, print "FizzBuzz."

n = int(input("Enter the number 1\n"))
for n in range(1, 100):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")