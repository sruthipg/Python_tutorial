class A(object):
    def start(self):
        print("In A")

class B(A):
    def start(self):
        print("In B")

ob=B()
ob.start()

# Inherit the parent class method from child class if the same method exist

