def choose_difficulty():
    """Returns number of attempts"""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("Please, try to choose difficulty again.")
        choose_difficulty()
    return attempts

def count_attempts(attempts, end_of_game):
    if attempts>0:
        attempts -=1
    elif attempts==0:
        print("You are out of attempts!")
        end_of_game = True
    return attempts, end_of_game