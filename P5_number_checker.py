# ask user for width and loop until they enter a number > 0

def num_check(question):
    error = "Please enter a number more than zero\n"
    while True:
        try:
            response = float(input(question))

            if response > 0:
            5    return response #ends loop
            else:
                print(error)

        except ValueError:  # prevents string input
            print(error)


# Main routine here
for item in range(0, 2):
    width = num_check("Width: ")
    print(width)

for item in range(0, 2):
    height = num_check("Height: ")
    print(height)

