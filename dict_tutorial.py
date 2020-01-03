'''

['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__',
  '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__',
  '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
  '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop',
  'popitem', 'setdefault', 'update', 'values']

'''

dict1={'a':"Apple",'b': "Ball",'c':"Cat",'d': "Dog"}
print(dir(dict1))
print("Length of dict",len(dict1))
print("Items",dict1.items())
print("Keys",dict1.keys())
print("Values",dict1.values())
# print("From Key",dict1.fromkeys(['a']))
print("Pop Item",dict1.popitem())
print("Pop ",dict1.pop('a'))
print(dict1)
print("Method1 Get",dict1.get('b'))
print("Method2 Get",dict1['c'])



