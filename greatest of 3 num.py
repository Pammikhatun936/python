'''write a program to find the greatest of 3 number entered by the user'''

a=int(input("enter a first number: "))
b=int(input("enter a second number: "))
c=int(input("enter a third number: "))
if(a>b and a>c):
    print("a is greater than b and c")
elif(a<b and b>c):
    print("b is greater than a and c")
else:
    print("c is greater than a and b")