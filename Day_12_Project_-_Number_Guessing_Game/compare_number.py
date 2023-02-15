def compare_number(chosen, guess, end_of_game):
    if guess>chosen:
        print("Too high.\nGuess again.")
    elif guess<chosen:
        print("Too low.\nGuess again.")
    elif guess == chosen:
        print("Correct! You won!")
        end_of_game = True
    return end_of_game
        