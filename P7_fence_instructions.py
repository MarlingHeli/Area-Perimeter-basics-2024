#calculate the cost of fencing for a rectangular area
#units in metres, ask for cost of fencing per m

#recycle number checking function
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

#get input (ask user for width, length, and cost per metre)
keep_going = ""
while keep_going == "":

    print("Welcome to the fencing cost calculator\n---")

    width = num_check("What is the width (metres)? ")
    length = num_check("Height? ")
    cost = num_check("What is the cost of fencing per metre? ")

#calculate perimeter
    perimeter = 2*width + 2*length

#calculate cost of fencing (perimeter * cost / m)
    fencing_cost = perimeter*cost

#output perimeter and cost
    print(f"The perimeter of your fence is {perimeter} m")
    print(f"The cost of your fencing is ${fencing_cost}")

#ask user if they wish to do another calculation (<enter> to loop)
    keep_going = input("\nPress enter to go again or submit any other key to stop. ")

print("\nThank you for using the fencing cost calculator lol")