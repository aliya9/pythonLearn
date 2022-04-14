#Guess the number (using while loop)


while True:

    number = int(input("Please enter a number: "))

    if number == 18:
        print("Correct answer")
        break
    elif number < 18:
        print("You entered a smaller number ")
        print("Try again! ")
    elif number > 18:
        print("You entered a greater number ")
        print("Try again! ")
