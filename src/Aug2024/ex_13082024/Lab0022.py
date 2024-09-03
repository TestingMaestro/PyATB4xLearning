# What if we need formatted Output
# Lets say, given a number pi = 3.14159. Print the value restricted tp 2 or 3 decimal places o/p should be 3.14 or 3.146

# use string format [f"{}" Strings]

pi = 3.14159
print("Formatted number [2 dec places]: ", f"{pi:.2f}")
print("Formatted number: [3 deci places]", f"{pi:.3f}")
