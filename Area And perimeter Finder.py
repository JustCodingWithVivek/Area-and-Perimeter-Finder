from cmath import pi
from hashlib import new
from tkinter.messagebox import YES


print("\t\tWelcome to this mathematics game")
print("Type 1 for rectangle related values")
print("Type 2 for square related values")
print("Type 3 for triangle related values")
print("type 4 for circle related values")


Select= int(input("\nEnter Your choice: "))
choice =int(Select)


#This is for finding rectangle related values
if choice==1:
    l=int(input("\nEnter the length: "))
    b=int(input("\nEnter the breadth: "))
    print("\nThis the area of rectangle: ",l*b)
    print("\nThis is the perimeter of rectangle: ",2*(l+b))

#This is for finding square related values
if choice==2:
    s=int(input("\nEnter the side length: "))
    print("\nThis the area of square: ",s*s)
    print("\nThis is the perimeter of square: ",4*s)

#This is for finding triangle related values
if choice==3:
    b=int(input("\nEnter the base length: "))
    h=int(input("\nEnter the height: "))
    print("\nThis the area of triangle: ",1/2*b*h)
    print("\nThis is for finding perimeter of triangle")
    a=int(input("Enter 1st side: "))
    b=int(input("Enter 2nd side: "))
    c=int(input("Enter 3rd side: "))
    print("This is the perimeter of triangle: ",a+b+c)
   
#This is for finding circle related values
if choice==4:
    area= int(input("\nEnter the area:"))
    pi=3.14
    print("\nThis is the area of circle",pi*area*area)
    print("\nThis is for finding circumference of circle")
    radius=int(input("\nEnter the radius:"))
    print("\nThis is the Circumfernce of circle",2*pi*radius)

elif choice>=4:
    print("Invalid input!!")
