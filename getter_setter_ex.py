class Myclass:
    def __init__(self,cousename):
        self.coursename=cousename

        # Setter Method

    def set_coursename(self,coursename):
        self.coursename=coursename

        # Getter method

    def get_coursename(self):
        print(self.coursename)
        return self.coursename

ob=Myclass("Python")
ob.get_coursename()

# implementation of encapsulation
# to modify the value of course name Set Method

ob.set_coursename("Java")
ob.get_coursename()
# Python docs library  read more