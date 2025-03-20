# Gerard Pelletier
# 2/18/2025
# P2LAB2
# A python script using keys and a dictionary to calculate the amount of gallons of gas you will use depending on the car.


cars = {
    "Camaro": "18.21",
    "Prius": "52.36",
    "Model S": "110",
    "Silverado": "26",
}

cars_keys = cars.keys()
print(cars_keys)

print(*cars_keys, sep = ", ")

car_input = input("Enter a vehicle to see it's mpg: ")

car_mpg = cars[car_input]

print(f"The {car_input} gets {car_mpg} mpg.")

user_miles = float(input(f"How many miles will you drive your {car_input}?: "))

gas_needed = user_miles/float(car_mpg)

print(f"{gas_needed:.2f} gallon(s) of gas are needed to drive the {car_input} {user_miles} miles.")



