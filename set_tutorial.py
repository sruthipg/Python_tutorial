# remove duplicates and ascending order

mset={1, 2, 8, 4, 6, 8, 2, 8, 7, 6, 9, 5, 2, 4, 7}
mset2={6, 88, 7, 56, 9, 23}
print(dir(mset))
print(mset)

'''

['__and__', '__class__', '__contains__', '__delattr__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
 '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__',
  '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__',
   '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', 
   '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', 
   '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference',
    'difference_update', 'discard', 'intersection', 'intersection_update',
     'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
      'symmetric_difference_update', 'union', 'update']
      
'''

mUnion = mset | mset2
mIntersection = mset & mset2
mSymmetric_diff = mset-mset2
mSymmetric_diff2 = mset2-mset
mIsSubset = mset2.issubset(mset)
mIssupeset = mset.issubset(mset2)

print("Union : ", mUnion)
print("Intersection : ", mIntersection)
print("Difference1 : ", mSymmetric_diff)
print("Difference2 : ", mSymmetric_diff2)
print("SubSet : ", mIsSubset)
print("SuperSet : ", mIssupeset)

# List, tuple, String ordered collection
# Set and dictionaries are unordered collection
# ImMutable(Vlaues cannot be changed) : Number, String, Tuple
# Mutable(Values can be changed) : List, Dictionary, Set


