# Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:
# input- score - 89
# output- B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

score = int(input("Enter the Score\n"))

if 90 <= score <= 100:
    print("Grade A and Score:", score)
elif 80 <= score <= 89:
    print("Grade B and Score:", score)
elif 70 <= score <= 79:
    print("Grade C and Score:", score)
elif 60 <= score <= 69:
    print("Grade D and Score:", score)
else:
    print("Grade F [Fail]", score)
