import random
rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
paper = ('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')
scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

game_pictures = [rock, paper, scissors]

print("Welcome to rock, paper, scissors game!")

# User Input
user_input = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper, 2 for Scissors \n"))
print(f"You chose: {user_input}")
if user_input >= 0 and user_input <= 2:
    print(game_pictures[user_input])

#Computer Choice
computer_choice = random.randint(0, 2)
print(f"Computer chose: {computer_choice}")
print(game_pictures[computer_choice])

#You won You Lose
if user_input >= 3 or user_input < 0:
    print("You typed an invalid number. Restart Now!")
elif computer_choice == 0 and user_input == 2:
    print("You Lose!")
elif computer_choice > user_input:
    print("You Lose!")
elif user_input > computer_choice:
    print("You Win!")
elif computer_choice == user_input:
    print("It's a draw!")