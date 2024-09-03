squares = [1, 4, 9, 16, 25]

squares.sort(reverse=False)

# 9 pop(pos)--> index is optional
# Removes item at the specified index
# if no index is specified, it removes last element
# default value is -1

x = squares.pop(len(squares) - 2)
print(x)
print(squares)

x = squares.pop(1)
print(x)
print(squares)

# 10. index(element)---> returns the index of an element in the list

y = squares.index(25)
print(y)
