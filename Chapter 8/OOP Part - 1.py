"""class Student:
    #name = "karan"
    #default constructor
    def __init__(self):
        pass
    
    #parametrized constructors
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        #print("adding new student in database..")
    
    def welcome(self): #method
        print("welcome student", self.name)

s1 = Student("karan", 97)
#print(s1.name, s1.marks)
s1.welcome()

s2 = Student("arjun", 96)
print(s2.name, s2.marks)



class Car:
    color = "Blue"
    brand = "Mercedes"

car1 = Car()
print(car1.color)
print(car2.brand)


#Static Method
class Student:
    @staticmethod   #decorator
    def hello():
        print("hello")

s1 = Student()
s1.hello()"""


#Abstraction, hiding unnecessary details from users and showing only essential details.
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.clutch = True
        self.acc= True
        print("car started..")

car1 = Car()
car1.start()

#Encapsulation, 

