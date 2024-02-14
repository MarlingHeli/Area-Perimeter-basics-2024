# ask user for width and loop until they enter a number > 0

def num_check(question):
    error = "Please enter a number more than zero\n"
    while True:
        try:
            response = float(input(question))

            if response > 0:
                return response  # ends loop
            else:
                print(error)

        except ValueError:  # prevents string input
            print(error)


# Main routine starts here

keep_going = ""
while keep_going == "":
    # get width and height
    width = num_check("Width (rectangle): ")
    height = num_check("Height: ")

    # calculate area/perimeter

    # display output
    area = width * height
    perimeter = width * 2 + height * 2

    print(f"The area of your rectangle is {area} cm")
    print(f"The perimeter of your rectangle is {perimeter} cm")

# ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. ")
    #this is where keep_going has the opportunity to be changed. if changed, the code will stop running.
    print()

print("Thank you for using the area/perimeter calculator.")
