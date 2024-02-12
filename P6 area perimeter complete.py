#ask the user for the width and height
# (assume they put in valid data)
def measurements():
    error = "Please enter a number higher than zero.\n"
    while True: #loop function until user inputs valid answers
        try:
          width = float(input("Please enter the width of your rectangle (cm): "))
          if width > 0:
              break
        except:
            print(error)
    while True:
        try:
            height = float(input("Please enter the height: "))
            if height > 0:
                break
        except:
            print(error)

#calculate the area/perimeter
    area = width*height
    perimeter = 2*width + 2*height
#output the area and perimeter
    print("The area of your rectangle is", area, "cm")
    print("The perimeter of your rectangle is", perimeter, "cm")

measurements()

