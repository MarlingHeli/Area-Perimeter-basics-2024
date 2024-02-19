#ask user for their name
username = input("What is your name? ")

#ask the user for their favourite number (integer)
fav_num = int(input("What is your favourite number? "))

double = fav_num * 2
halve = fav_num / 2
square = fav_num * fav_num

print(f"Hi {username}, your favourite number is {fav_num}")
#f stands for "format"
print(f"Your favourite number doubled is {double}")
print(f"Your favourite number halved is {halve}")
print(f"Your favourite number squared is {square}")
print("\nHave a nice day")