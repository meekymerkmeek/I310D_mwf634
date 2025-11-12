def calculate_volume_of_sphere(radius):
   from math import pi
   # Calculate the volume of a sphere given its radius
   return 4/3 * pi * radius ** 3


# Test cases
radius1 = 30
area1 = calculate_volume_of_sphere(radius1)
print(f"The volume of a sphere with a radius of {radius1} is: {area1}")

radius2 = 40
area2 = calculate_volume_of_sphere(radius2)
print(f"The volume of a sphere with a radius of {radius2} is: {area2}")

