# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.


class Student:
    def __init__(self,name,m1,m2,m3):
        self.name = name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def avg(self):
        avg = (self.m1+self.m2+self.m3)/3
        print(f"Average marks of {self.name} in 3 subjects are {avg}")

s1 = Student("Aksh",90,95,88)
s1.avg()