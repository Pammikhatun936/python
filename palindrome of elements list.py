''' write a program to check if a list contains a palindrome of elements (hints: use copy() method)'''

list=['m','o','m']
l1=list.copy()
l1.reverse()
if(list==l1):
    print("the given char is palindrome")
else:
    print("the given char is not palindrome")