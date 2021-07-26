#guessing game
n=18
attemp=5
print("Guess the number", end=":")
g=int(input())
while attemp>1:
    if g==18:
        print("Congratulations You Won\nYour score is:", attemp*20)
        print("Number of guesses you made: ", 6-attemp,  end="")
        break
    elif g>=18:
        print("you guessed number is greater than the actual one")
        attemp=attemp-1
        print("Attempts left:", attemp, "\nTry again", end=":")
        g=int(input())
        continue
    elif g<=18:
        print("you guessed number is less than the actual one")
        attemp=attemp-1
        print("Attempts left:", attemp, "\nTry again", end=":")
        g=int(input())
        continue
if attemp==1:
    print("Game over")