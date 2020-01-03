
'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__getitem__',
'__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__',
'__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
'__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal',
'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind',
 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


'__add__'
'__contains__'
__dir__
__doc__
__len__
join
split
'''


# Define String and check porperties
first_name="Sruthi"
middle_name='Padathara'
last_name='''George'''

print(first_name,middle_name,last_name)

# Change First Charcter of a String
# first_name[0]="M"
# print(first_name)
# TypeError: 'str' object does not support item assignment

# First name replaced by Unni
first_name= "UnniKrishnan"
print(first_name)

# Join Strings
full_name= first_name+" "+middle_name+" "+last_name
print("Fullname : %s" %(full_name))

# String Formatting
# Method1
print("My FirstName is %s and My Middle Name is %s and My Last Name is %s"%(first_name,middle_name,last_name))

# Method2
age=30
intro="My Name is %s and My age is %d"
print(intro %(full_name,age))

los=len(first_name)
print("Length of First Name",los)

print(dir(first_name))

# Search for a word return true is value contains else false
search=full_name.__contains__("")
print(search)

# Add will add the string at the end of the String
ss=full_name.__add__(" aaa ")
print(ss)

# Spilt will sp;it the string with delimiter specified
a=ss.split(" ")
print(a)

# If only one character specified will print that character
# print the "jstrStr" (no. character-1) times
pan=first_name.join("ZZZZ")
print(pan)

# Return the position of the particular character
mFind=first_name.find("i")
print(mFind)

# Numbers


['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__',
 '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__',
 '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__',
 '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__',
 '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__',
 '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__',
 '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__',
 '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__',
 '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator',
 'real', 'to_bytes']

a=10
print(dir(a))
b=20

# Add a and b
mSum=a.__add__(b)
print(mSum)

mAnd=a.__and__(b)

