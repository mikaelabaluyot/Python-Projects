import random

print("Welcome to Rock, Paper, Scissors!")

#choices
choices = ['rock', 'paper', 'scissors']


user_choose= int(input("Take a number: (1 for rock, 2 for paper, 3 for scissors)"))


if user_choose < 1 or user_choose > 3:
    print("Please try again! Insert a number between 1 and 3")
else:
    user_choose -= 1

    computer = random.randint(0,2)

    print(f"You choose: {choices[user_choose]}")
    print(f"Computer chose: {choices[computer]}")

    if user_choose == computer:
        print("It's a tie!")
    elif (user_choose == 0 and computer == 2) or \
         (user_choose == 1 and computer == 0) or \
         (user_choose == 2 and computer == 1):
        print("You win!")
    else:
        print("Computer wins!")