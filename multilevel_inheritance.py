class A(object):
    def start(self):
        print("In A")

class B(A):
    def start(self):
        print("In B")
class C(B):
    pass

ob=C()
ob.start()
# using super can refer to parent
