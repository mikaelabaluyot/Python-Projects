#def name():
  # The code inside

import random

def fortune_cookie():
    fortune_cookie = random.randint(0,6)
    if fortune_cookie == 1:
        print("Don't pursue happiness – create it")
    elif fortune_cookie == 2:
        print("All things are difficult before they are easy.")
    elif fortune_cookie == 3:
        print("The early bird gets the worm, but the second mouse gets the cheese.")
    elif fortune_cookie == 4:
        print("The fortune you search for is in another cookie.")
    elif fortune_cookie == 5:
        print("Someone in your life needs a letter from you.")
    elif fortune_cookie == 6:
        print("Your heart will skip a beat.")
    else:
        print("Help! I'm being held prisoner in the cookie bakery!")


fortune_cookie()



