'''

['__add__', '__class__', '__contains__', '__delattr__',
'__delitem__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__',
 '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__',
 '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
  '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__',
   '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append',
   'clear', 'copy', 'count', 'extend', 'index', 'insert',
   'pop', 'remove', 'reverse', 'sort']

'''


list1 = [2, 8, 6, 8, 9, 8, 5, 2]
list2 = [[5, 5, 8, 6, 4], [5, 8, 5, 5, 5], (5, 8, 9, 6), 56]

# Updating list will point to the same memory location
print("ID : ", id(list1))
list1.append(12)
print("ID2 : ", id(list1))

print(dir(list1))
print("List2 Type", type(list2))
print("List1 Type", type(list1))

print(list1)
print(list2)

subList = list1[1:3]
print("Slicing :", subList)
subList1 = list1[::2]
print("Slicing 1 :", subList1)
subList2 = list1[::-1]
print("Slicing Reverse :", subList2)

print("Size", list1.__sizeof__())
print(type(list1[0]))

print("Pop 2nd element", list1.pop(2))



