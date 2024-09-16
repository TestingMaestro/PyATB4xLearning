# Find max element in the list



class Maximum:
    my_list = [20, 30, 50, 60, 90]
    is_flag = False

    def __init__(self):
        self.maxi = int(input("Enter the number"))

    def maximum1(self):
        for i in range(len(self.my_list)):
            if self.maxi > self.my_list[i]:
                self.is_flag = True
                print("maximum")
                break
            else:
                print("Minimum")
                break


maxi = Maximum()
maxi.maximum1()
