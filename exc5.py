#tuples -- are immutable like string sin java
three_numbers = (1,2,3)
print(three_numbers)
print(three_numbers[2])
a = len(three_numbers)


## functions ##
def batman(a,b):
    print('hello ji')
    return a+b

def greeting(*names):
    print('welcome' + names[2])

print(greeting('abhay','hi','kl'))
print(batman(3,6))


