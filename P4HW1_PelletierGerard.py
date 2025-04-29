# Gerard Pelletier
# 3/25/2024
# P4HW1
# Using loops for more efficient and dynamic coding

num_scores = int(input("How many scores do you want to enter?: "))
gradeslist=[]

for each in range(num_scores):
    score = int(input(f"Enter score #{each+1}: "))
    while score < 0 or score > 100:
        print("INVALID Score entered!!!")
        print("Score should be between 0 and 100")
        score = int(input(f"Enter score #{each+1} again: "))
    gradeslist.append(score)
    

print(gradeslist)

print("-"*10, "Results", "-"*10)
print(f"{'Lowest Score:':<15}{min(gradeslist)}")
gradeslist.remove(min(gradeslist))
print(f"{'Modified List:':<15}{gradeslist}")
avg = sum(gradeslist) / len(gradeslist)
print(f"{'Average:':<15}{avg:.2f}")
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')
print("-"*29)

# sorry for lacking any pseudocode here, i just feel more comfortable writing actual code