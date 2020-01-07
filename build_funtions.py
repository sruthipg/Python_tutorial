list1=['a','b','c']
enlsit=enumerate(list1)
print(list(enlsit))

for i in enumerate(list1):
    print(i)


a=[1,2,3]
at=all([len(a)>2, a[1]==2])
print(at)
af=all([len(a)>2, a[1]==1])
print(af)

ant=any([len(a)>=3,a[1]==2])
print(ant)


anf=any([len(a)>3,a[1]==3])
print(anf)