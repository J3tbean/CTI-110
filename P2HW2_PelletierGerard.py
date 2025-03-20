# Gerard Pelletier
# 2/25/2025
# P2HW1
# Learning about lists.

gradeslist=[]

grade_1 = float(input("Enter grade for Module 1: "))
grade_2 = float(input("Enter grade for Module 2: "))
grade_3 = float(input("Enter grade for Module 3: "))
grade_4 = float(input("Enter grade for Module 4: "))
grade_5 = float(input("Enter grade for Module 5: "))
grade_6 = float(input("Enter grade for Module 6: "))

gradeslist.append(grade_1)
gradeslist.append(grade_2)
gradeslist.append(grade_3)
gradeslist.append(grade_4)
gradeslist.append(grade_5)
gradeslist.append(grade_6)

print(gradeslist)

print()
print("-"*10, "Results", "-"*10)
print(f"{'Lowest Grade:':<15}{min(gradeslist)}")
print(f"{'Highest Grade:':<15}{max(gradeslist)}")
print(f"{'Sum of Grades:':<15}{sum(gradeslist)}")
print(f"{'Average:':<15}{sum(gradeslist) / len(gradeslist):.2f}")
print("-"*29)