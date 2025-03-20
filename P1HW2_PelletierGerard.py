# Gerard Pelletier
# 2/11/2025
# P1HW2
# A python program that does budgeting math for you.

budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")

gas = int(input("How much do you think you will spend on gas? "))
hotel = int(input("Approximately, how much will you need for accomodation/hotel? "))
food = int(input("Last, how much do you need for food? "))

print("------Travel Expenses------")
print("Location:", destination)
print("Initial Budget:", budget)

print("Fuel:", gas)
print("Accomodation:", hotel)
print("Food:", food)

print("Remaining Balance:", str(budget - gas - hotel - food))