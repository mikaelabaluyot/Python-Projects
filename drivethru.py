def get_item(x):
    if x == 1:
        return '🍔 Cheeseburger'
    elif x == 2:
        return '🍟 Fries'
    elif x == 3:
        return '🥤 Soda'
    elif x == 4:
        return '🍦 Ice Cream'
    elif x == 5:
        return '🍪 Cookie'
    else:
        return '404. Item not found.'

def welcome():
  print('Welcome to the drive_thru!')
  print('Menu:')
  print('1. 🍔 Cheeseburger')
  print('2. 🍟 Fries')
  print('3. 🥤 Soda')
  print('4. 🍦 Ice Cream')
  print('5. 🍪 Cookie')

welcome()

item = int(input("Please choose a number: "))

print(get_item(item))
