def cube(num):
    return num*num*num
def hello(num):
    '''hello I am Ani and I want to be a company owner when I grow up'''
    if num % 3==0:
        return cube(num)
    else:
        return False
print(hello(6))
print(hello(2))
print(hello(66))
print(hello(22))
print(hello(62))
print(hello(26))
print(hello.__doc__)