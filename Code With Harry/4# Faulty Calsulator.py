 print("Enter first number:")
a = input()
print("Enter operator:")
c = input()
print("Enter second number:")
b = input()
if a==45 and b==3 and c=="*":
    d=555
elif a==3 and b==45 and c=="*":
    d=555
elif a==56 and b==9 and c=="+":
    d=77
elif a==9 and b==56 and c=="+":
    d=77
elif a==56 and b==6 and c=="/":
    d=4
elif a==6 and b==56 and c=="/":
    d=4
else:
    if c=="*":
    d = int(a)*int(b)
    elif c=="+":
    d = int(a)+int(b)
    elif c=="-":
    d =  int(a)-int(b)
    elif c=="/":
    d = int(a)/int(b)

print(d)