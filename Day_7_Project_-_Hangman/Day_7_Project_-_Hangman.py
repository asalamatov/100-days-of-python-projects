import random
from hangman_art import stages, logo
from hangman_word_list import word_list
import os

chosen_word = random.choice(word_list)
display = ["_" for _ in range(len(chosen_word))]
final_word = ""
lives = 6
end_of_game = False


print(logo)
print("Welcome to the Hangman Game!")

while not end_of_game:
    user_choice = input("Guess a letter: ").lower()
    os.system("cls")
    
    if user_choice in display:
        print(f"You have already guessed '{user_choice}'.")
     
    for i in range(len(chosen_word)):
        if user_choice==chosen_word[i]:
            display[i]=user_choice
            
    if user_choice not in chosen_word:
      print(f"The letter '{user_choice}' is not in the word.")
      lives-=1
      if lives == 0:
        print("You lose.")
        end_of_game=True
        print(f"The word was {chosen_word}.")
            
    print(f"{' '.join(display)}")
            
    
    
    if "_" not in display:
        end_of_game=True
        print("You win!")
        
    print(stages[lives])
    

