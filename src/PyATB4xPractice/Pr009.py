# ✅ Triangle Classifier:

len1 = int(input("Enter the length 1\n"))
len2 = int(input("Enter the length 2\n"))
len3 = int(input("Enter the length 3\n"))


def triangle_classifier(l1, l2, l3):
    if l1 == l2 == l3:
        return "Equilateral Triangle"
    elif l1 == l2 or l2 == l3:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"


res = triangle_classifier(l1=len1, l2=len2, l3=len3)
print(res)
