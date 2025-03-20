# Gerard Pelletier
# 2/18/2025
# P2LAB1
# A python script for calculating the diameter, circumference and area of a circle.

radius = float(input("What is the radius of the circle?:"))
pi = float("3.141592653589793")
diameter = float(2*radius)
circumference = float(2*pi*radius)
area = float(pi*radius**2)

print(f"Radius of the circle is {radius}.")
print("")
print(f"The diameter of the circle is {diameter:.1f}.")
print("")
print(f"The circumference of the circle is {circumference:.2f}.")
print("")
print(f"The circumference of the circle is {area:.3f}.")
print("")