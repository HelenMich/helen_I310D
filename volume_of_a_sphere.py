import math

def calculate_volume_of_sphere_(radius):
    volume = (math.pi * (radius ** 3)) * (4/3)
    return volume

radius1 = 30
volume1 = calculate_volume_of_sphere_(radius1)
print(f"The volume of sphere with radius {radius1} is: {volume1}")

radius2 = 40
volume2 = calculate_volume_of_sphere_(radius2)
print(f"The volume of sphere with radius {radius2} is: {volume2}")