# Gerard Pelletier
# 3/4/2025
# P3LAB
# Using else/if to divide numbers into dollars and coins

money = float(input("Enter amount of money as a float: $"))

money = int(money * 100)

num_dollars = money // 100
money = money - (num_dollars * 100)

if money == 0:
    print(f"No Change")


if num_dollars > 1: 
    print(f"{num_dollars} Dollars")
elif num_dollars == 1:
    print(f"{num_dollars} Dollar")

num_quarters = money // 25
money = money - (num_quarters * 25)

if num_quarters > 1: 
    print(f"{num_quarters} Quarters")
elif num_quarters == 1:
    print(f"{num_quarters} Quarter")

num_dimes = money // 10
money = money - (num_dimes * 10)

if num_dimes > 1: 
    print(f"{num_dimes} Dimes")
elif num_dimes == 1:
    print(f"{num_dimes} Dime")

num_nickles = money // 5
money = money - (num_nickles * 5)

if num_nickles > 1: 
    print(f"{num_nickles} Nickles")
elif num_nickles == 1:
    print(f"{num_nickles} Nickle")

num_pennies = money 

if num_pennies > 1: 
    print(f"{num_pennies} Pennies")
elif num_pennies == 1:
    print(f"{num_pennies} Penny")