from art import logo, vs
from os import system
from game_data import data
from random import choice

def clear():
    system("cls")
    
def check_answers(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess=="a"
    else:
        return guess=="b"

def get_random_account():
    return choice(data)

def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f'{name}, a {description}, from {country}'

def game():
    clear()
    print(logo)
    score = 0
    end_of_game = False
    account_a = get_random_account()
    account_b = get_random_account()
    
    while not end_of_game:
        account_a = account_b
        account_b = get_random_account()
        
        while account_a == account_b:
            account_b = get_random_account()
        
        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").lower().strip()
        a_f_count = account_a['follower_count']
        b_f_count = account_b['follower_count']
        is_correct = check_answers(guess, a_f_count, b_f_count)
        
        clear()
        print(logo)
        if is_correct:
            score +=1
            print(f"You are right! Current score: {score}")
        else:
            end_of_game = True
            print(f"Sorry, that's wrong. Final score: {score}")
            

game()
        
        
        