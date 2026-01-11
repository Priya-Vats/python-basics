#Guess the number

"""import random

target = random.randint(1,100)

while True:
    userchoice = input("guess the target or Quit(Q):")
    if(userchoice == "Q"):
        break

    userchoice = int(userchoice)
    if(userchoice == target):
        print("Success : correct guess!!")
        break

    elif(userchoice < target):
        print("your number was too small. Take a bigger guess...")

    else:
        print("your number was too big. Take a smaller guess...")


print("----GAME OVER-----")"""


#Randome Password Generator

import random
import string

#print(string.ascii_letters)
#print(string.digits)
#print(string.punctuation)

password_len = 12
charvalues = string.ascii_letters + string.digits + string.punctuation

#list comprehension[function for i in range()

res = "".join([random.choice(charvalues) for i in range(password_len)])
print(res)



#print(charvalues)
#password = ""
#for i in range(password_len):
    #password += (random.choice(charvalues))

#print("your random password is:", password)


#print(random.choice("hello"))
#val = random.choice(['a','b','c', 'd', 'e', 'f'])
#print(val)