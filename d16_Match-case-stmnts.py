# Day 16

# Match case statements

# Match case are available from python 3.10 onwards !!!IMPORTANT

x = 5

match x:
    case 0:
        print("x is 0")
        # Break statement is not mandatory
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case 3:
        print("x is 3")
    case 4:
        print("x is 4")

    case _ if x != 90:
        print(x, ' is not 90')
        print('Case 5')
    case _ if x != 80:
        print(x, ' is not 80')
    case _:
        print("x is not 0, 1, 2, or 3")