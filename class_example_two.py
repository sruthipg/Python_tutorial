class Second():
    def __init__(self):
        self.__pr="I am Private"
        self._pro="I am Protected"
        self.pub="I am public"

obj=Second()

# accessing public object
print(obj.pub)
# Changing value of public attribute
obj.pub=obj.pub+" We can modify public attribute"

print(obj.pub)
# Accessing protected variable and modifying it
print(obj._pro)
obj._pro=obj._pro + " We can modify Protected too"
print(obj._pro)

# Trying to access private members
# print(obj.__pr)
print(obj._Second__pr) # can access the private
# can check the level of naming conventional using the _pri, __pro,pub
# bz the lang should not come as barrier for the developer
# AttributeError: 'Second' object has no attribute '__pr'


obj._Second__pr=obj._Second__pr+" 123"
print(obj._Second__pr)# can modify also
# https://mail.python.org/pipermail/tutor/2003-October/025932.html

