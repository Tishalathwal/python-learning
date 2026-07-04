# Problem: Create a function that returns both the area and circumference of a circle given its radius.



import math

def circle(radius):
    area=math.pi * radius ** 2
    circumference=2 * math.pi * radius
    return area, circumference 

print(f"The area and circumference of a circle with radius 5 is: {circle(5)}")