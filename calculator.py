def add(a,b):
    result=a+b
    print("a+b= ",result)

def sub(a,b):
    result=a-b
    print("a-b= ",result)

def mul(a,b):
    result=a*b
    print("a*b= ",result)

def div(a,b):
    result=a/b
    print("a/b= ",result)

a=int(input("Enter the first number: "))
op=input("Enter the operator: ")
b=int(input("Enter the second number: "))

if op=="+":
    add(a,b)
elif op=="-":
    sub(a,b)
elif op=="*":
    mul(a,b)
elif op=="/":
    div(a,b)
else:
    print("Invalid Operation")