#Find the greater of three

a = int(input("a :"))
b = int(input("b :"))
c = int(input("c :"))

if(a>b):
    if (a>c):
        print("a is greater")
elif(b>c):
    if(b>a):
        print("b is greater")
elif(c>a):
    if(c>b):
        print("c is greater")
else:
    print("All equal")


#Find the greater of four

a = int(input("First Num :"))
b = int(input("Second Num :"))
c = int(input("Third Num :"))
d = int(input("Fourth Num :"))

if(a>b and a>c and a>d):
    print("The larger number is :", a)
elif(b>a and b>c and b>d):
    print("The larger number is :", b)
elif(c>a and c>b and c>d):
    print("The larger number is :", c)
else:
    print("The larger number is :", d)