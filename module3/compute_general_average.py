""" module3/compute_general_average.py

Uses basic math operations and while loops to compute the general average of a student.

"""

IS_WRITING = True
grades = []

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
