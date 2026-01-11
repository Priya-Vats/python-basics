light = input("light color :")

if(light == "red"):
    print("STOP")
elif(light == "yellow"):
    print("READY")
elif(light == "green"):
    print("GO")
else:
    print("light is broken")

marks = int(input("marks : "))
#arks = 75
if(marks >= 90):
    print("A")
elif(marks >= 80 and marks <90):
    print("B")
elif(marks >= 70 and marks <80):
    print("C")
else:
    print("D")

#Nesting

age = 95
if(age>=18):
    if(age>= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")