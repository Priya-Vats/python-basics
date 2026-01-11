"""dict = {
    "chem" : input("Chem:"),
    "Phy" : input("Phy:"),
    "Maths" : input("Maths:"),
}

print(dict)"""

marks = {}

x = int(input("enter phy:"))
marks.update({"phy" : x})

y = int(input("enter chem:"))
marks.update({"chem" : y})

z = int(input("enter maths:"))
marks.update({"maths" : z})

print(marks)