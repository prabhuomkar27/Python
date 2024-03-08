import random

# Guess the number

def guess_number():
    secret_number = random.randint(1,5)
    attempts = 0

    while True:
        guess = int(input("Guess the number (between 1 and 5): "))
        attempts=attempts+1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts ")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

# Play the game
guess_number()
