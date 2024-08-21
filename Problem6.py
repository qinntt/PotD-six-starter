def string_oder_int(inpt):
    #please make some code that returns true if the input is a integer or a string if neither return -1
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
def letter_and_s(inpt):
    # plesae make code that tests if the inpt is a string and the letter s
    return -1

def treat_input(inpt):
        try:
            if str(inpt).count('.') == 1:
                return float(inpt)
            else:
                return int(inpt)
        except:
            return str(inpt)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 6:
        
        holder  = treat_input(sys.argv[1])
        holder1 = treat_input(sys.argv[2])
        holder2 = treat_input(sys.argv[3])
        holder3 = treat_input(sys.argv[4])
        holder4 = treat_input(sys.argv[5])

        print(string_oder_int(holder))
        print(len0x(holder1))
        print(len0xOrder(holder2, holder3))
        print(letter_and_s(holder4))