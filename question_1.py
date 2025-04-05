# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.


# my method

class Student:
    def __init__(self,name,m1,m2,m3):
        self.name = name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def avg(self):
        avg = (self.m1+self.m2+self.m3)/3
        print(f"Average marks of {self.name} in 3 subjects are {avg}")

# s1 = Student("Aksh",90,95,88)
# s1.avg()


# best method

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks 

    def Gavg(self):
        sum = 0
        i = 0
        for mar in self.marks:
            sum+=mar
            i+=1

        print(f"Average marks of {self.name} are {sum/i}")
        

s2 = student("Aksh", [90,95,88])
s2.Gavg()