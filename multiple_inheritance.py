class A(object):
    def start(self):
        print("In A")

class B(A):
    def start(self):
        print("In B")

class C(B,A):
    pass

ob = C()
ob.start()
print(dir(ob))
print(C.__mro__) #Method resolution order
# current, left, right based on algorithm ?
# python history blogspot 2010 Read more


# Check by adding super one by one class


# Inherit the parent class method from child class if the same method exist

