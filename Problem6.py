def string_oder_int(inpt):
    #please make some code that tests if the input is a integer or an string
    return -1
def len0x(inpt):
    # please make some code that tests if the input is a ingteger.
    # if it isn't return -1 other wise return the len of a binary version of that int.
    return -1
def len0xOrder(int1, int2):
    # please make code that tests if both inputs are an integer
    # and will return negative one if either are not 
    # then will return the larger of the two
    return -1

if __name__ == "__main__":
    import sys
    print(string_oder_int(4.1))
    print(string_oder_int(4))
    print(len0x(10))
    print(len0x('10'))
    print(len0xOrder(1,3))
    print(len0xOrder('2',3))
    if len(sys.argv) == 3:
        print(string_oder_int(sys.argv[0]))
        print(len0x(sys.argv[1]))
        print(len0xOrder(sys.argv[2]))