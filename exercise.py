# name='Abhinav"
# o/p = "A$B$h$I$N$V
name='Abhinav'
print("Splitted: ",name.split())
print("Listed : ",list(name))
print('$'.join(list(name)))

import funtion_examples
print("I am in exercise.py")
funtion_examples.func3()
if __name__ == '__main__':
    print("exercise is getting executed directly")
else:
    print("exercise.py if being imported %s"%__file__)



