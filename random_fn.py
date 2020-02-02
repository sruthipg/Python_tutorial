import random as rd

a=list(range(4,10,2))
print(a)

print("Random Single : ",rd.randrange(10))
print("Rand range1 : ",rd.randrange(4,100))
print("Rand range : ",rd.randrange(4,100,5))
print("Rand Int : ",rd.randint(5,9))

print("GetState : ",rd.getstate)
print("Uniform : ",rd.uniform(5,10))
