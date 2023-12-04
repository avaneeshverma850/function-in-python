'''x=5
print("x=",x)
a=int(input("enter a number"))
c=a**2
print("square of",a,"is",b)'''
#here we call a function  
'''def f1():
    x=20
    print(x)
f1()
f1()
f1()
f1()'''
#once function is defined it can be called any number of times
#varaible created inside the function body are called local variable
#Takes something return nothing
'''def f1(y):
    b=y**2
    print("square of",y,"is",b)
def start():
    x=5
    f1(x)
start()'''
#takes something return something
'''def f1(y):
    b=y**2
    #print("square of",y,"is",b)
    return b
def start():
    x=6
    result=f1(x)
    print(result)
start()'''
#takes something ,return nothing
'''def add(a,b):
    c=a+b
    print("sum is",c)
add(10,20) #actual argument'''
#Takes nothing ,return something
'''def add():
    print("enter two numbers")
    a=int(input())
    b=int(input())
    c=a+b
    return c
s=add()
print("sum is",s)'''
#takes something ,return something
'''def add(a,b):
    c=a+b
    return c
result=add(10,20)
print(result)'''

