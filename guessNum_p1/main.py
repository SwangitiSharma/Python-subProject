import random
ranNum = random.randint(1, 100)
userGues = None
guesses = 0

while(userGues != ranNum):
    userGues = int(input("Enter your guess: "))
    guesses += 1
    if(userGues==ranNum):
        print("You guessed it right!")
    else:
        if(userGues>ranNum):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")

print(f"You guessed the number in {guesses} guesses")




