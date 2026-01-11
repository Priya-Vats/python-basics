#WAF(Funtion) to print the length of a list. (list is the parameters)
Marks = [64, 77, 55, 66, 98, 43, 48]
Heroes = ["ironman", "thor", "spiderman", "hulk"]

def list_len(list):
    print(len(list))
    return list

list_len(Marks)
list_len(Heroes)


#WAF to print the elements of a list in a single line. (list in the parameter)

marks = [64, 77, 55, 66, 98, 43, 48]

def print_list(list):
    for item in list:
        print(item, end = " ")

print_list(marks)

#WAF to find the factorial of n.(n is the parameter)

#way 1
n = 10
f = 1
def fact_orial(n,f):
    for el in range(1 , n+1):
        f *= el
        print("factorial:", f)

fact_orial(n,f)

#way 2
n = 5

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        print("factorial:", fact)

cal_fact(5)

#WAF to convert USD to INR

def converter(usd_val):
    inr_val = usd_val*83
    print(usd_val, "USD =", inr_val, "INR")


converter(100)



#Home work problem

#n = int(input("Enter the number:"))
def Number(n):
    Mod = n%2
    if (n%2==0):
        print("EVEN")
    else:
        print("ODD")

Number(17)
