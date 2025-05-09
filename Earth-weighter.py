

print('Planet Weights')

earth_weight = float(input("Enter weight of your Earth: "))
planet_number = int(input("Enter a planet number (1-7): "))

## destination_weight = earth_weight * relative_gravity

if planet_number == 1:
    print(earth_weight * 0.38)
elif planet_number == 2:
    print(earth_weight * 0.91)
elif planet_number == 3:
    print(earth_weight * 0.38)
elif planet_number == 4:
    print(earth_weight * 2.53)
elif planet_number ==5:
    print(earth_weight * 1.07)
elif planet_number == 6:
    print(earth_weight * 0.89)
elif planet_number == 7:
    print(earth_weight * 1.14)
else:
    print('Invalid planet number')


print('Planet Weights')

relative_gravity = {
    1: 0.38, # Mercury
    2: 0.91, # Venus
    3: 0.38, # Mars
    4: 2.53, # Jupiter
    5: 1.07, # Saturn
    6: 0.89, # Uranus
    7: 1.14  # Neptune
}

earth_weight = float(input("Enter weight of your Earth: "))
planet_number = int(input("Enter a planet number (1-7): "))

## destination_weight = earth_weight * relative_gravity

if planet_number in relative_gravity:
    print(earth_weight * relative_gravity[planet_number])
else:
    print('Invalid planet number')



