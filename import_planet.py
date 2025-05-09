from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)

if random_planet == 'Mercury':
    r = 2440

elif random_planet == 'Venus':
    r = 6052
elif random_planet == 'Earth':
    r = 6371
elif random_planet == 'Mars':
    r = 3390
elif random_planet == 'Saturn':
    r = 58232

else:
    print("Oops! An error occurred.")

planet_area = 4 * pi * r * r

planet_name = input("Insert a planet: ")

print(f'Area of {random_planet}: {planet_area} sq mi')




