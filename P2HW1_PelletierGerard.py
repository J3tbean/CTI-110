# Gerard Pelletier
# 2/25/2025
# P2HW1
# Learning about string formatting.
print("This program calculates and displays travel expenses")
print()
budget = float(input("Enter Budget: "))
print()
travel = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you will spend on gas?: "))
print()
hotel = float(input("Approximately, how much will you need for accomodation/hotel?: "))
print()
food = float(input("Last, how much do you need for food?: "))
print()
remaining = float(budget - gas - hotel - food)

print("-" * 10, "Travel Expenses", "-" * 10)

print(f"{'Location:':<20}{travel}")
print(f"{'Initial Budget:':<20}${budget:.2f}")
print(f"{'Fuel':<20}${gas:.2f}")
print(f"{'Accomodation:':<20}${hotel:.2f}")
print(f"{'Food:':<20}${food:.2f}")
print("-" * 20)

print()
print(f"{'Remaining Balance:':<20}${remaining:.2f}")
print()
print()