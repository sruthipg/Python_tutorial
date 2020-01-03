# Arithmetic, Assignment, Comparison, Logical, Bitwise, Identity, Membership

# ArithMetic Operation
# ______________________________________________________

a=5
b=2
madd=a+b
msub=a-b
mmul=a*b
mdiv=a/b
mmod=a%b
mExp=a**b
mfloor_div=a//b

print("Addition : ", madd)
print("Subtraction : ", msub)
print("Multiplication : ", mmul)
print("Division : ", mdiv)
print("Modulus : ", mmod)
print("Exponential : ", mExp)
print("Floor Division : ", mfloor_div)

# Assignment Operations
# ________________________________________________________

s = a
print(a)
print(s)

a=b
print(a)
print(b)

b=s
print(b)

# Logical Operations
# __________________________________________________________

a=20
b=200
c=0
print("And Op : ", (a and b))
print("And with 0 : ", a and c)
print("And Op2", (b and a))
print("And2  with 0", c and a)

print("OR Op : ", (a or b))
print("OR with 0 : ", a or c)
print("OR Op2", (b or a))
print("OR with 0", c or a)

# Bitwise Operations
# ___________________________________________________________

a = 60
b = 80
c = 0
d = -1

# Bitwise AND sets the bits in the result to 1 if both the corresponding bits in the two operands are 1.

print("Bitwise AND")
print("A & B : ", (a & b))
print("A & C : ", (a & c))
print("A & D : ", (a & d))

print("Bitwise OR")
print("A | B : ", (a | b))
print("A | C : ", (a | c))
print("A | D : ", (a | d))


print("Bitwise XOR")
print("A ^ B : ", (a ^ b))
print("A ^ C : ", (a ^ c))
print("A ^ D : ", (a ^ d))

print("Bitwise NOT")
print("NOT A : ", (~a))
print("NOT C : ", (~c))
print("NOT D : ", (~d))

# A left shift by n bits is equivalent to multiplication by
# pow(2, n). A long integer is returned if the result exceeds the range of plain integers.
print("Bitwise LEFT SHIFT")
print("A << B : ", (a << b))
print("A << C : ", (a << c))

# Negative shift counts are illegal and cause a ValueError to be raised.
# print("A << D : ", (a << (d)))

print("Bitwise RIGHT SHIFT")
print("A >> B : ", (a >> b))
print("A >> C : ", (a >> c))
# Negative shift counts are illegal and cause a ValueError to be raised.
# print("A >> D : ", (a >> (d)))

