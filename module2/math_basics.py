""" module2/math_basics.py

Demonstrate basic math operations in Python using if-else statements.

"""
print("module2/math_basics.py.py\n")

print(
    "This program has four functions:\nA --- Add two numbers\nB --- Add 3 numbers, multiply by ",
    "one hundred, and subtracted by 21\nC --- Multiply 4 numbers and divide it by 4\nD --- ",
    "Compute the GWA of a student\n",
)

OPTION = str(input("Enter the function you want to use [A/B/C/D]: "))

if OPTION.lower() == "a":
    print("A --- Add two numbers\n")
    firstNumber = int(input("Enter first number: "))
    secondNumber = int(input("Enter second number: "))
    print("The sum of the two numbers is: ", firstNumber + secondNumber)
elif OPTION.lower() == "b":
    print("B --- Add 3 numbers, multiply by one hundred, and subtracted by 21\n")
    firstNumber = int(input("Enter first number: "))
    secondNumber = int(input("Enter second number: "))
    thirdNumber = int(input("Enter third number: "))
    print("The result is: ", (firstNumber + secondNumber + thirdNumber) * 100 - 21)
elif OPTION.lower() == "c":
    print("C --- Multiply 4 numbers and divide it by 4\n")
    firstNumber = int(input("Enter first number: "))
    secondNumber = int(input("Enter second number: "))
    thirdNumber = int(input("Enter third number: "))
    fourthNumber = int(input("Enter fourth number: "))
    print(
        "The result is: ", (firstNumber * secondNumber * thirdNumber * fourthNumber) / 4
    )
elif OPTION.lower() == "d":
    IS_WRITING = True
    grades = []

    print("D --- Compute the GWA of a student")
    print(
        "This program will enter write mode, if you are done entering your grade and want to ",
        "exit write mode, just type 'done'.\n",
    )
    while IS_WRITING:
        userInput = input("Enter your grade [12345/done]: ")
        if userInput.lower() == "done":
            IS_WRITING = False
        elif userInput.isnumeric():
            grades.append(int(userInput))
        else:
            print("Invalid input, enter a number or 'done'.\n")

    print("\nYour grades are: ", grades)
    print("Your GWA is: ", sum(grades) / len(grades))
else:
    print("Invalid input, enter A/B/C/D.")
