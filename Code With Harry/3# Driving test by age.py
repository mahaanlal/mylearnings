print("Enter your age", end=":")
age = int(input())
if 100 > age > 7 :
    if age > 18 :
        print("Yes you can Drive")
    elif age == 18:
        print("We will think abut it")
    else:
        print("You cannot Drive")
else:
    print("Kindly enter a valid age")