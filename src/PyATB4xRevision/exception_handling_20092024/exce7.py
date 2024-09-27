# NESTED TRY EXCEPT

try:
    try:
        a = float(input("Enter 1st number"))
        b = a + a
    except AttributeError as e:
        print(e)
    else:
        print(f"addition:{b}")
except Exception as e:
    print(e)

