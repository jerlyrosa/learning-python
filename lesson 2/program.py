# program.py
sum = 1 + 2 # 3

product = sum * 2

print(product)

print("show this in the console")

# type of data

planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string

print(type(planets_in_solar_system))

print(type(distance_to_alpha_centauri))

print(type(can_liftoff))

print(type(shuttle_landed_on_the_moon))

# Dates
from datetime import date

print("Today's date is: " + str(date.today()))