import sys

num1=float(sys.argv[1])
operation=sys.argv[2]
num2=float(sys.argv[3])

def add(num1,num2):
    result=num1+num2
    return result

def sub(num1,num2):
    result=num1-num2
    return result

def mul(num1,num2):
    result=num1*num2
    return result


if operation =="+":
    print(add(num1,num2))
elif operation =="-":
    print(sub(num1,num2)) 
else:
    print(mul(num1,num2))
          
