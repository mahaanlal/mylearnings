#Exercise 5
#Video 38 is solution
#Health Management system

def getdate():
    import datetime
    return datetime.datetime.now()
print("Welcome to CodeWithHarry Gym :)")
name = str(input("Enter Name:"))
name = name.capitalize()
a = str(input("what do you want to log?\nPress d for diet or press e for exercise:"))
while 1:
    if a=="e" or a=="d":
        break
    else:
        print("Try again:")
        a = str(input("what do you want to log?\nPress d for diet or press e for exercise:"))
f = open(f"{name}_{a}.txt", "a+" )
f.close()
f = open(f"{name}_{a}.txt", "r+" )
print(f.read())

ask = str(input("Do you want to enter a new value?\nPress y for yes:"))
if str(ask)=="y":
    if a==str("d"):
        f.write(f"Time: {getdate()} | Diet: ")
        f.write(str(input("Enter diet:")))
        f.write("\n")
    elif a==str("e"):
        f.write(f"Time: {getdate()} | Exercise: ")
        f.write(str(input("Enter Exercise:")))
        f.write("\n")

print("Time:", getdate())
f.close()
print("\nStay Healthy and stay fit\nThank you and Goodbye")