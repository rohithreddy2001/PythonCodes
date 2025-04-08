import random

def guess_game():
    secret_number = random.randint(1, 100)
    guesses = []
    attempts = 0
    max_attempts = 10  # New: set a limit

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts.")

    while attempts < max_attempts:  # Changed from True to a limit
        try:
            guess = input("Enter your guess: ")
            guess = int(guess)
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue
            guesses.append(guess)
            attempts += 1

            if guess < secret_number:
                print(f"Too low! {max_attempts - attempts} attempts left.")
            elif guess > secret_number:
                print(f"Too high! {max_attempts - attempts} attempts left.")
            else:
                print(f"Congrats! You got it in {attempts} attempts!")
                print(f"Your guesses were: {guesses}")
                if len(guesses) > 1:  # Fun feedback with the list
                    print(f"Your closest wrong guess was: {min(guesses[:-1], key=lambda x: abs(x - secret_number))}")
                break
        except ValueError:
            print("Please enter a valid number!")

    if attempts == max_attempts:  # If you run out of tries
        print(f"Game Over! The number was {secret_number}.")
        print(f"Your guesses were: {guesses}")

guess_game()