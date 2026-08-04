import random 

random_num = random.randint(1, 100)

guesses = []

user_guess = None

while user_guess != random_num:
    user_guess = int(input("pick a number between 1 and 100: "))
    guesses.append(user_guess)
    if user_guess > random_num:
        print("Too high!")
    elif user_guess < random_num:
        print("Too low!")

print(f"correct! Here's how many times you guessed: {len(guesses)}, here are your guess: {guesses}")

