''' search for a number x in this tuple using loop:
   (1,4,9,16,25,36,49,64,81,100)''' 

tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x=int(input("enter the number to search: "))
i=0
while i < len(tuple):
    if tuple[i] == x:
      print("found")
   
    i=i+1
