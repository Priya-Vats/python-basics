#arithmatic operators
a = 5
b = 2

#sum = a + b
#print(sum)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) #remainder
print(a ** b) #a^b


#Relational operators return boolean values , True or False
a = 50
b = 40

print(a == b) #False
print(a != b) #True
print(a >= b) #True
print(a <= b) #False
print(a < b) #False
print(a > b) #True 


#Assignment Operators
num = 10
#num = num +10
num += 10
print("num :", num) #20

num -= 10
print("num :", num) #10

num *= 10
print("num :", num) #100

num /= 10
print("num :", num) #10

num %= 10
print("num :", num) #0

num **= 10 #power operator
print("num :", num) #0


#Logical Operators
a = 50
b = 30
print(not False)
print(not (a > b))

val1 = True
val2 = False
print("AND operator: ",val1 and val2) 

print("OR operator: ",(a == b) or (a > b)) 

