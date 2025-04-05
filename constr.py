class Student:
   

    def __init__ (self,name,rollno):
        print("Student constructor")
        self.name = name
        self.rollno = rollno
       
        print("Name = "  ,name)
        print("rollno = "  ,rollno)
       
        print("Student of particular data is complete")

s1 = Student("Aksh",5)
s2 = Student("Akshat",15)


