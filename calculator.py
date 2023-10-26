def calculator(x,y,n):
    if n=='+':
        print(x+y)
    elif n=='-':
        print(x-y)
    elif n=='/':
        if y!=0:
            print(x/y)
        else:
            print("error:division by zero")
    elif n=='*':
        print(x*y)
    elif n=='%':
        if y!=0:
            print(x%y)
        else:
            print("error:modulo by zero")
    else:
        print("invalid operator")
x=float(input("enter first value:"))
y=float(input("enter second value:"))
n=input("enter operator(+,_,*,/,%):")

calculator(x,y,n)
