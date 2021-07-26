#Taking inputs
print("Enter the number of  lines \nof the triangle you want to print:", end="")
n = int(input())
while True:
    print("Press 1 for upwards pointing triangle \n"
          "or"
          "\nPress 0 for downwords pointing triangle", end=":")
    b = int(input())
    if b==1 or b==0:
        break
    else :
        print("\nKindly try again\n")

#Checking conditions and print stars
if bool(b)==True:
    j=0
    while j<n:
        j=j+1
        i = 0
        print("")
        #Printing stars
        while i < j:
            print("*", end=" ")
            i = i + 1
elif bool(b)==False:
    while n>0:
        n=n-1
        print("")
        #Printing stars
        i = 0
        while i < n+1:
            print("*", end=" ")
            i = i + 1