count = 0


def increment():
    global count
    count += 1
    print(count)


for i in range(89):
    increment()

