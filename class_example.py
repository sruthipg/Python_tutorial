class Myclass():

    # Put restiction
    domain ="Python for Data Science"

    def SetCourse(self,name):
        self.name=name

ob1=Myclass()
ob2=Myclass()
ob1.SetCourse("Python")
ob2.SetCourse("Java")

print(ob1.domain)
print(ob1.name)
print(ob2.domain)
print(ob2.name)

# self.name is able to call using te object
# self current calling obj. internally ob1.name,
# ob2.name ='Java' is associated with instance of the class
# ob1 & ob2 are different instance
# domian is class level attributes will always give the same result

