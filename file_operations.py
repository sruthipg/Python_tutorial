import os

f=open('/home/user/sruthi/Tutorial/Tutorial/Docs/sample','r')
print(dir(f))
'''
['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', 
'__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__',
 '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', 
 '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', 
 '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', 
 '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
  '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', 
  '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 
  'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 
  'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'seek', 
  'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines']

'''
print("Beg :",f.tell())
print("First", (f.read()))
print("First End :",f.tell())
f.seek(0)
print("Second", (f.read()))
print("Second End :",f.tell())

f.seek(0)
print("Afetr Seek", f.tell())


f.seek(12)
print("Afetr sec Seek", f.tell())

with open('/home/user/sruthi/Tutorial/Tutorial/Docs/sample', 'a') as fl:
    print(fl.tell())
    fl.write("\n 2,5,8,6,5,5,6")



nf=open("sample.txt","w+")
for i in range(1,10):
    nf.write("\n Hello, Welcome to python")

for i in range(1,10):
    print(nf.read())
nf.seek(0)

print(nf.tell())

os.rename("sample.txt", "Turorial.txt")
# os.remove("Tutorial.txt")
# start from beg and go to 4th location
print(nf.seek(4,0))
print("After Seek beg", nf.tell())

# start from current location  and go to 4th location
print(nf.seek(4,1))
print("Seek from current ", nf.tell())


print("Particular : ", nf.read())
for i in nf:
    print(i)
# REad individual line
nf.close()

