#Private attributes

"""class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Priya")
print(s1.name)
del s1.name
print(s1.name)

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345", "abcde")

print(acc1.acc_no)
#print(acc1.acc_pass)
print(acc1.reset_pass()) """


#Inheritence
"""class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")
 
class ToyotaCar(Car):
    def __init__(self,brand):
        self.name = brand

class Fortuner():
    def _init__(self,type):
        self.type = type
    

#car1 = ToyotaCar("fortuner")
#car2 = ToyotaCar("prius")

#print(car1.name)
#print(car1.color)

car1 = Fortuner("diesel")
car1.start()"""

#Multiple Inheritence

"""class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)"""


#Class method

"""class Person:
    name = "anonymous"

    #def changename(self,name):
        #self.name = name
        #Person.name = name
        #self.__class__.name = "arjun"
        #self.__class_-.Person.

    @classmethod
    def changename(cls,name):
        cls.name = name

p1 = Person()
p1.changename("arjun kumar")
print(p1.name)
print(Person.name)"""


#Property

"""class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        #self.percentage = str((self.phy + self.chem + self.maths) / 3) + "%"

    #def calcpercentage(self):
        #self.percentage = str((self.phy + self.chem + self.maths) / 3) + "%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.maths) / 3) + "%"

stu1 = Student (60,75,45)
print(stu1.percentage)
#percentage

stu1.phy = 70
#print(stu1.phy)
#stu1.calcpercentage()
print(stu1.percentage)"""


#Polymorphism
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real,"i +" , self.img,"j")

    #def add(self, num2):
        #newREAL = self.real + num2.real
        #newIMG  = self.img + num2.img
        #return Complex(newREAL, newIMG)

    def __add__(self, num2):
        newREAL = self.real + num2.real
        newIMG  = self.img + num2.img
        return Complex(newREAL, newIMG)


num1 = Complex(1,3)
num1.shownumber()

num2 = Complex(4,6)
num2.shownumber()

#print(num1+ num2)
num3= num1+ num2
#num3 = num1.add(num2)
num3.shownumber()
