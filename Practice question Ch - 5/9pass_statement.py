#write a program to find the sum of first natural numbers.(using while)

"""n = int(input("Enter the number:"))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print("total sum :", sum)"""

#write a program to ffind the factorial of first n numbers.(using for)

n = 10
fact = 1

for el in range(1 , n+1):
    fact *= el
    print("factorial:", fact)