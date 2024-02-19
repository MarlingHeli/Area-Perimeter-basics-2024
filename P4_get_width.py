#ask user for width and loop until they enter a number > 0
error = "Please enter a number more than zero\n"

while True:

    try:
        width = float(input("Width: "))

        if width > 0:
            break #ends loop
        else:
            print(error)

    except: #prevents string input
        print(error)