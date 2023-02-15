from art import logo
from choose_difficulty import choose_difficulty, count_attempts
from chosen_number import number
from clean_screen import clean
from compare_number import compare_number

clean()
print(logo)

start_number = 1
end_number = 100
end_of_game = False

print("Welcome to the Number Guessing Game!")
number_of_attempts = choose_difficulty()
print(f"I am think of a number between {start_number} and {end_number}.")
chosen_number = number(start_number, end_number)

while not end_of_game:
    print(f"You have {number_of_attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    end_of_game = compare_number(guess=guess, chosen=chosen_number, end_of_game=end_of_game)
    number_of_attempts, end_of_game = count_attempts(number_of_attempts, end_of_game=end_of_game)
    
    
    





