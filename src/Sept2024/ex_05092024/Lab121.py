# Encapsulation
# Biding wrapping the data members within the class using private access specifiers and using methods only
# Parent  class securing its attributes using access specifiers and by using methods only
class MyClass:
    # Public variable
    my_public_var = "I am PUBLIC"

    # Protected variable ['_'--> single underscore]
    _my_protected_var = "I am PROTECTED"

    # Private variable ['__'--> double underscore]
    __my_private_var = "I am PRIVATE"


obj = MyClass()
# print(obj.my_public_var)
# print(obj._my_protected_var)
print(obj.__my_private_var)
