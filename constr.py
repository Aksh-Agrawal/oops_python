class Student:
   

    def __init__(self):
        print("default construnctor") #default construnctor
        pass

    def __init__ (self,name,rollno): #constructor (parametrized)
        
        self.name = name
        self.rollno = rollno
       
        print("Name = "  ,name)
        print("rollno = "  ,rollno)
       
        print("Student of particular data is complete")

s1 = Student("Aksh",5) #object
s2 = Student("Akshat",15)


