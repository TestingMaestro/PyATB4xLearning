"""
Task #10 -
✅ Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24

"""
# Logic 1
num = int(input("Enter the number\n"))
fact1 = 1
sn = "*"
for i in range(num, 0, -1):
    fact1 = fact1 * i
    print(f"{i}*", end=" ")
print("=", fact1)

# Logic 2
"""
fact = 1
for i in range(num, 0, -1):
    for j in range(i, 0, -1):
        print(f"{j}", end=" ")
        fact = fact * j
    print("=", fact)
    fact = j
"""

