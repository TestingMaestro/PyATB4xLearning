userGrade = input("User Grade\n")
userGrade = userGrade.upper()
match userGrade:
    case "A":
        print("Garde A")
    case 'B':
        print("Grade B")
    case 'C':
        print("Grade C")
    case _:
        print("Fail")
