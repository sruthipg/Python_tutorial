import math as mt

print(dir(mt))

# Math Theoretic Funtions
# Ceil will round the next integer and returns
print("Rounded : ",mt.ceil(10.1))
# x,y returns the sign of the y (-ve,+ve)
print("Copy Sign : ",mt.copysign(9.8,-1))
# Always returns the positive integer
print("Fabs : ", mt.fabs(-19.1))

# Power and Logarithmic Funtion
print("Eponential : ",mt.exp(2))
# Element-wise exponential minus one: out = exp(x) - 1. This is a scalar if x is a scalar.
# This function provides greater precision than exp(x) - 1 for small values of x.

print("Expnential ML : ",mt.expm1(2))

print("Log Single",mt.log(5))
print("Log with Base",mt.log(5,10))

# Trigonometric Funtion
# Arc values should be  (-,+) 0 to 1(0,.1,.2,..,.9,1)
# Returns the values in radians
print("Arc Sine",mt.asin(1))
print("Sine",mt.sin(5))
print("Arc Cos",mt.acos(.5))
print("Cos",mt.cos(5))
print("Arc Tan",mt.atan(.5))
print("Tan",mt.tan(5))

# Angular Hyperbolic Functions
# Convert angle x from radians to degrees
print("Degrees : ",mt.degrees(.1))
print("Radians : ",mt.radians(5.729577951308233))
print("Pi value : ",mt.pi)
print("Const e : ",mt.e)