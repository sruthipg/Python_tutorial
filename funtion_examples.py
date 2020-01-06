
# def {identifier}({arguments}):
#     {body}


def add(a, b):
    res = a + b
    print("a :", a)
    print("b :", b)
    return res
    # res=res+2
outpt = add(b=5,a=3)
print(outpt)

def add(c):
    print(3.14 * c)

add(2)

def fun1(username,pwd,*args):
    print("Type of the value passed",type(args))
    print("Agruments",args)


fun1("Sruthi","123",24,58.55,',hhh',True)

def fun2(username,**args):
    print("Type of the value passed",type(args))
    print("Agruments",args)

fun2('44',hjj='15')

def func3():
     print("func3() in function_examples.py")

print("I am in function_examples.py")

if __name__ == '__main__':
    print("function_examples is getting executed directly")
else:
    print("function_examples.py if being imported %s"%__file__)





