from calendar import c
from cmath import pi
from hashlib import new
from tkinter.messagebox import YES


print("\t\t***Welcome to this Mathematics Game***")
print("Type 1 for Rectangle related values")
print("Type 2 for Square related values")
print("Type 3 for Triangle related values")
print("Type 4 for Circle related values")
print("Type 5 for Paralellogram related values")
print("Type 6 for Trapezium related values")
print("Type 7 for Rhombus related values")
print("Type 8 for Kite related values")

Select= int(input("\nEnter Your choice: "))
choice =Select

#This is for finding rectangle related values---(CCJustCodingWithVivek)
if choice==1:
    print("You Entered and Finding Rectangle Related Values")
    l=int(input("\nEnter the length: "))
    b=int(input("Enter the breadth: "))
    print("\nThis the Area of Rectangle: ",l*b)
    decision = input("\nType Yes For Finding Perimeter else No ")
    if decision=="Yes":
        print("\nThis is the Perimeter of Pectangle: ",2*(l+b))
        print("Thankyou for using Mathematics Game")
    else:
        print("Thankyou for using Mathematics Game")
    

#This is for finding square related values---(CCJustCodingWithVivek)
if choice==2:
    print("You Entered and Finding Square Related Values")
    s=int(input("\nEnter the side length: "))
    print("This the Area of Square: ",s*s)
    decision = input("\nType Yes For Finding Perimeter else No ")
    if decision=="Yes":  
        print("/nThis is the Perimeter of Square: ",4*s)
        print("Thankyou for using Mathematics Game")
    else:
        print("Thankyou for using Mathematics Game")

#This is for finding triangle related values---(CCJustCodingWithVivek)
if choice==3:
    print("You Entered and Finding Triangle Related Values")
    b=int(input("\nEnter the base length: "))
    h=int(input("Enter the height: "))
    print("\nThis the Area of Triangle: ",1/2*b*h)
    decision = input("\nType Yes For Finding Perimeter else No ")
    if decision=="Yes":
        s1=int(input("Enter 1st Side: "))
        s2=int(input("Enter 2nd Side: "))
        s3=int(input("Enter 3rd Side: "))
        print("\nThis is the Perimeter of Triangle: ",s1+s2+s3)
        print("Thankyou for using Mathematics Game")
    else:
        print("Thankyou for using Mathematics Game")
   
   
#This is for finding Circle related values---(CCJustCodingWithVivek)
if choice==4:
    decision=(input("Do you want to use the value of π in decimal ??(Yes/No) :"))

    if decision=="Yes":
        print("π = 3.14")
        x = 3.14
        r = float(input("Enter the Radius of the Circle: "))
        area = x*(r**2)
        print("The Area of the Circle is:",area)
        decision = input("\nType Yes For Finding Perimeter else No ")
        if decision=="Yes":
            ("/nThis is the Circumfernce of Circle",2*pi*r)
            print("Thankyou for using Mathematics Game")
        elif decision=="No":
            print("Thankyou for using Mathematics Game")
    
    elif decision=="No":
        print("π = 22/7")
        pie = 22/7
        r = float(input("Enter the Radius of the Circle: "))
        area = float(pie)*float(r)*float(r)
        print("The Area of the Circle is:",area)
        decision = input("\nType Yes For Finding Perimeter else No ")
        if decision=="Yes":
            print("/nThis is the Circumfernce of Circle",2*pi*r)
            print("Thankyou for using Mathematics Game")
        elif decision=="No":
            print("Thankyou for using Mathematics Game")
    
        else :
            print ("invalid input")
            print("Thankyou for using Mathematics Game")

#This is for finding Paralellogram related values---(CCJustCodingWithVivek)
if choice==5:
    print("You Entered and Finding Paralellogram Related Values")
    l=int(input("\nEnter the length: "))
    b=int(input("Enter the breadth: "))
    print("\nThis the Area of Paralellogram: ",l*b)
    decision = input("\nType Yes For Finding Perimeter else No ")
    if decision=="Yes": 
        print("\nThis is the Perimeter of Paralellogram: ",2*(l+b))
        print("Thankyou for using Mathematics Game")
    else:
        print("Thankyou for using Mathematics Game")

#This is for finding Trapezium related values---(CCJustCodingWithVivek)
if choice==6:
    print("You Entered and Finding Trapezium Related Values")
    a=int(input("\nEnter the 1st Side: "))
    b=int(input("Enter the 2nd Side: "))
    h=int(input("Enter the height: "))
    print("\nThis the Area of Trapezium: ",a+b/2*h )
    decision = input("\nType Yes For Finding Perimeter else No ")
    if decision=="Yes":
        c=int(input("Enter the 3rd Side: "))
        d=int(input("Enter the 4th Side: "))   
        print("\nThis is the Perimeter of Trapezium: ",a+b+c+d)
        print("Thankyou for using Mathematics Game")
    else:
        print("Thankyou for using Mathematics Game")

#This is for finding Rhombus related values---(CCJustCodingWithVivek)
if choice==7:
    print("You Entered and Finding Rhombus Related Values")
    d1=int(input("\nEnter the 1st diagonal length: "))
    d2=int(input("Enter the 2nd diagonal length: "))
    print("\nThis the Area of Rhombus: ",d1*d2/2 )
    decision = input("\nType Yes For Finding Perimeter else No ")
    if decision=="Yes":
        s=int(input("Enter the Side Length: "))   
        print("\nThis is the Perimeter of Rhombus: ",s*4)
        print("Thankyou for using Mathematics Game")
    else:
        print("Thankyou for using Mathematics Game")

#This is for finding Rhombus related values---(CCJustCodingWithVivek)
if choice==8:
    print("You Entered and Finding Kite Related Values")
    d1=int(input("\nEnter the 1st diagonal length: "))
    d2=int(input("Enter the 2nd diagonal length: "))
    print("\nThis the Area of Kite: ",d1*d2/2 )
    decision = input("\nType Yes For Finding Perimeter else No ")
    if decision=="Yes":
        s=int(input("Enter the Side Length: "))
        p=int(input("Enter the Side Length: "))   
        print("\nThis is the Perimeter of Kite: ",2*(s+p))
        print("Thankyou for using Mathematics Game")
    else:
        print("Thankyou for using Mathematics Game")

else:
    print("\nInvalid input!!!")
