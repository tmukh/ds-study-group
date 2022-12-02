def found_float(st):
    point =0
    for i in st:
        if i.isdigit():
            continue
        elif i == ".": 
            point+=1
        else:
            return False
    if point == 1:
        return True
    return False

def get_type(x):
    try:
        x.decode('utf-8')
        print("This was a byte")
    except AttributeError:
        if x.isdigit():
            print("This was an integer")
        elif found_float(x):
            print("This was a float")
        elif x == "True" or x == "False":
            print("This was a bool")
        elif x == "None":
            print("This was a NoneType")
        else:
            print("This was a string")

again = True
while again:
    inp = input("Enter characters: ")
    print(f"The type is now {type(inp)}")
    get_type(inp)
    again = input("Try again? Enter True to continue or False to stop\n")
    if again == "True":
        continue
    elif again == "False":
        print("Thanks for your attention")
        break
    else:
        again = input("Wrong input. Enter True to continue or False to stop\n")
