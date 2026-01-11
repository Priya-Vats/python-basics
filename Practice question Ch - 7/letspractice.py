"""with open("Practice question Ch - 7/practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programmingin Java.")

with open("Practice question Ch - 7/practice.txt","r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("Practice question Ch - 7/practice.txt","w") as f:
    f.write(new_data)"""

with open("Practice question Ch - 7/practice.txt","r") as f:
    data = f.read()
    if(data.find("learning")!= -1):
        print("found")
    else:
        print("not found")

