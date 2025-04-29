# Gerard Pelletier
# 3/20/2025
# P4LAB1
# More loop practice.

run_again = "yes"
while run_again != "no":
    integer = int(input("Enter an integer: "))

    if integer >= 0:
        for i in range(1,13):
            print(f"{integer} * {i} = {integer * i}")
    else:
            print("This program does not handle negative numbers.")
    run_again = input("Would you like to run the program again?: ")

print("Ok, Goodbye!")