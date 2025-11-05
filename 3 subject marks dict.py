'''write a program to enter marks of 3 subjects from the user and store them in a dictionary .start with an empty 
 dictionary & add one by one .use subjects name as key & marks as values'''

marks= {}

x=int(input("enter maths: "))
marks.update({"maths" : x})

x=int(input("enter biology: "))
marks.update({"biology" : x})

x=int(input("enter physics: "))
marks.update({"physics" : x})

print(marks)
