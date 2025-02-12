# 049: Number guessing game
compnum = 50
attempts = 0

while True:
    guess = int(input("Guess the number: "))
    attempts += 1
    if guess < compnum:
        print("Too low, try again.")
    elif guess > compnum:
        print("Too high, try again.")
    else:
        print("Well done, you took", attempts, "attempts.")
        break