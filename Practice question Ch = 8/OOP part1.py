#Create student class that takes name & marks of 3 subjects as arguments in constructer. then create a method to print the average
"""class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in  self.marks:
            sum += val
        print("hi", self.name, "your average score is:", sum/3)

s1 = Student("tony stark", [99,98,97])
xs1.get_avg()"""


#Create account class with 2 attributes - balance & account no. / Create a method for debit, credit & printing the balance
class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

        #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs." , amount, "was debited")
        print("total balance = ", self.get_balance())

    #credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs." , amount, "was credited")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(5000)