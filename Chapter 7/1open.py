#reading to a file
"""f = open("Chapter 7/demo.txt","rt")
data = f.read(5)
print(data)
line1 = f.readline()
print(line1)
print(type(data))
f.close()"""


#writing to a file

"""f = open("Chapter 7/demo.txt","w")
f.write("I want to learnjavasvript tomorrow. 123")
f.close()

f = open("Chapter 7/demo.txt","a")
f.write("\nThen I'll move to reactJS")
f.close()

f = open("Chapter 7/sample.txt", "a")
f.close()"""


#With syntax

"""with open("Chapter 7/demo.txt", "r") as f:
    data = f.read()
    print(data)

with open("Chapter 7/demo.txt", "w") as f:
    f.write("new data")"""


import os
os.remove("Chapter 7/sample.txt")
