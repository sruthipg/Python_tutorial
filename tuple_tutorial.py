
tup1=(5,8,9,4,12)
print(tup1)
ele=tup1[4]
print(ele)

# TypeError: 'tuple' object does not support item assignment
# uptup=tup1[0]=11
# print(uptup)

'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
 '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', 
 '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', 
 '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
 '__repr__', '__rmul__', '__setattr__', '__sizeof__', 
 '__str__', '__subclasshook__', 'count', 'index']

'''

print(dir(tup1))
print("Length of Tuple :", len(tup1))
print("Max of Tuple :", max(tup1))
print("Min of Tuple :", min(tup1))
print("Sum of Tuple :", sum(tup1))
print("Type of Tuple :", type(tup1))

# If element is present it returns true else false
print("Check of element",tup1.__contains__(5))
# multiplies the tuple speciifed no. of times
print("Multipliction : ", tup1.__mul__(2))

list1=list(tup1)
print("Tuple to List",list1)
print("List to Tuple",tuple(list1))
print(tup1)

# get item fro index
print("Item with inbuild fn :",tup1.__getitem__(3))

