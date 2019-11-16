# Challenge 032
import math
radius = int(input("Enter the radius of a circle: "))
depth = int(input("Enter the depth of a cylinder: "))
area = math.pi * (radius**2)
total_volume = area * depth
print(round(total_volume, 3))
