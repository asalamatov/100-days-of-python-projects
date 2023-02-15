import random

print('''
Welcome to Rock Paper Scissors Game
What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.
''')

user_choice = input()
computer_choice = random.randint(0,2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

if user_choice in ["0","1","2"]:
    user_choice=int(user_choice)
    print("You chose: ")
    print(game_images[user_choice])
    print("Computer chose: ")
    print(game_images[computer_choice])
    if user_choice==computer_choice:
        print("It is a Draw.")
    elif (user_choice == 2 and computer_choice == 1) or (user_choice==1 and computer_choice==0) or (user_choice==0 and computer_choice==2):
        print("You Win!")
    else:
        print("You lose.")
else:
    print("Invalid input")
    

