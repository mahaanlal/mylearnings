while 1:
    print("Enter a number", end=":")
    n = int(input())
    if n>100:
        print ("Congratulations you have entered a number greater than 100")
        break
    else:
        print("Sorry, Try again")
        continue