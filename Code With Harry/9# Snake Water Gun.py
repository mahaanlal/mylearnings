#make a game and display score
#Video 41/129 CodeWithHarry
import random
username = input("_Hello Gamer_\nEnter your name:")
userscore = 0
computerscore = 0
for i in range(10):
    print(f"\n----------Round {i + 1}----------\n")
    while True :
        user = input("Choose one s/w/g :")
        user = user.casefold()
        if user=="s" or user=="w" or user=="g":
            if user == "s":
                user = "Snake"
            elif user == "w":
                user = "Water"
            elif user == "g":
                user = "Gun"
            computer = ["Snake", "Water", "Gun"]
            c = random.choice(computer)
            choices =[user, c]
            if choices==["Snake", "Water"] or choices==["Water", "Gun"] or choices==["Gun", "Snake"]:
                userscore = userscore+1
            elif choices==["Snake", "Gun"] or choices==["Water", "Snake"] or choices==["Gun", "Water"]:
                computerscore = computerscore + 1

            print(f"{username}: {user}\nComputer: {c}")
            print(f"Scoreboard--->{username}: {userscore}  Computer: {computerscore}")
            break
        else:
            print("Enter a valid input!!!")
            continue
#Results
if userscore > computerscore:
    print("-----Congratulatins!!!-----\n     -----YOU WON-----")
elif userscore == computerscore:
    print("-----GAME DRAW-----")
else:
    print("-----YOU LOSE-----")
