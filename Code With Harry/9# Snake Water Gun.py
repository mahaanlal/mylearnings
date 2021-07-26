#make a game and display score
#Video 41/129 CodeWithharr
import random
while 1:
    user = input("Choose one s/w/g :")
    if user=="s" or user=="w" or user=="g":
        break
    else:
        print("Enter a valid input")
#for computer1
c1 = random.randint(1,3)
if c1==1:
    c1 = "snake"
elif c1==2:
    c1 = "Water"
elif c1==3:
    c1="Gun"

#for computer2
c2 = random.randint(1,3)
if c2==1:
    c2 = "snake"
elif c2==2:
    c2 = "Water"
elif c2==3:
    c2="Gun"

print(f"You: {user}\nComputer1: {c1}\nComputer2: {c2}")

def gam(a,b,c):
    if [a,b,c]==[s,w,g]: