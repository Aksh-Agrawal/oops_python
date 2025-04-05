class teacher:
    collage = "Csvtu" #attributes
    name = "outside"
    def __init__(self,name):
        self.name = name

    def welcome(self):
        print("Second fxn", self.name)

t1 = teacher("idk")

print(t1.collage)
print(teacher.name)
t1.welcome()