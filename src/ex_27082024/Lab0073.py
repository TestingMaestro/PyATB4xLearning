public_toilet = "PB"


def home():
    private_toilet = "PT"
    print(private_toilet)
    # print(public_toilet) # used before initialization
    public_toilet = "LPB"  # becomes local variable masks the global var value
    print(public_toilet)


#
def stranger():
    # print(private_toilet) # Error--. local variable cannot be used outside
    print(public_toilet)


home()
stranger()
