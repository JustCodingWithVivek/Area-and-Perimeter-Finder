from calendar import c
from cmath import pi
from hashlib import new
from tkinter.messagebox import YES
import time

while (True):

#Designing
    p_1="-------------------------------------------------------------------"
    p_2="--------------------------------------------------"
    p_3="----------------------------------------"

#Main body
    print(p_1)
    print("\t**** Welcome to this Mathematics Game ****")
    print(p_1)
    print("Type 1 for Rectangle related values")
    print("Type 2 for Square related values")
    print("Type 3 for Triangle related values")
    print("Type 4 for Circle related values")
    print("Type 5 for Paralellogram related values")
    print("Type 6 for Trapezium related values")
    print("Type 7 for Rhombus related values")
    print("Type 8 for Kite related values")
    print(p_1)

    Slt= int(input("Enter Your choice: "))
    print(p_1)
    choice =Slt

#This is for finding rectangle related values---(CCJustCodingWithVivek)
    if choice==1:
        print("You Entered and Finding Rectangle Related Values")
        print(p_2)
        l=int(input("Enter the length: "))
        b=int(input("Enter the breadth: "))
        print(p_3)
        print('Processing.')
        time.sleep(3)       
        print("\nThis the Area of Rectangle: ",l*b)
        print(p_2)
        decision = input("Type Yes For Finding Perimeter else No ")
        if decision.capitalize()=="Yes":
            print(p_2)
            print('Processing.')
            time.sleep(3)  
            print("\nThis is the Perimeter of Rectangle: ",2*(l+b))
            print(p_2)
            print("")
            print(p_1)
        else:
            print(p_1)
            print("Thankyou for using Mathematics Game")
            print(p_1)

#This is for finding square related values---(CCJustCodingWithVivek)
    if choice==2:
        print("You Entered and Finding Square Related Values")
        print(p_1)
        s=int(input("Enter the side length: "))
        print(p_3)
        print('Processing.')
        time.sleep(3)  
        print("\nThis the Area of Square: ",s*s)
        print(p_2)
        decision = input("Type Yes For Finding Perimeter else No ")
        print(p_2)
        if decision.capitalize()=="Yes":
            print('Processing.')
            time.sleep(3)    
            print("\nThis is the Perimeter of Square: ",4*s)
            print(p_2)
            print("Thankyou for using Mathematics Game")
            print(p_1)
        else:
            print(p_1)
            print("Thankyou for using Mathematics Game")
            print(p_1)
#This is for finding triangle related values---(CCJustCodingWithVivek)
    if choice==3:
        print("You Entered and Finding Triangle Related Values")
        print(p_1)
        b=int(input("\nEnter the base length: "))
        h=int(input("Enter the height: "))
        print(p_3)
        print('Processing.')
        time.sleep(3)  
        print("\nThis the Area of Triangle: ",1/2*b*h)
        print(p_2)
        decision = input("Type Yes For Finding Perimeter else No ")
        if decision.capitalize()=="Yes":
            print(p_3)
            s1=int(input("Enter 1st Side: "))
            s2=int(input("Enter 2nd Side: "))
            s3=int(input("Enter 3rd Side: "))
            print(p_3)
            print('Processing.')
            time.sleep(3)  
            print("\nThis is the Perimeter of Triangle: ",s1+s2+s3)
            print(p_2)
            print("Thankyou for using Mathematics Game")
            print(p_1)
        else:
            print(p_1)
            print("Thankyou for using Mathematics Game")
            print(p_1)
   
#This is for finding Circle related values---(CCJustCodingWithVivek)
    if choice==4:
        decision=(input("Do you want to use the value of π in decimal ??(Yes/No) :"))
        print(p_1)

        if decision.capitalize()=="Yes":
            print("π = 3.14")
            print(p_3)
            x = 3.14
            r = float(input("Enter the Radius of the Circle: "))
            area = x*(r**2)
            print(p_3)
            print('Processing.')
            time.sleep(3)  
            print("\nThe Area of the Circle is:",area)
            print(p_2)
            ecision = input("Type Yes For Finding Perimeter else No ")
            if decision.capitalize()=="Yes":
                print('Processing.')
                time.sleep(3)
                print("\nThis is the Circumfernce of Circle",2*pi*r)
                print(p_2)
                print("Thankyou for using Mathematics Game")
                print(p_1)
            elif decision.capitalize()=="No":
                print(p_1)
                print("Thankyou for using Mathematics Game")
                print(p_1)
    
        elif decision.capitalize()=="No":
            print("π = 22/7")
            print(p_3)
            pie = 22/7
            r = float(input("Enter the Radius of the Circle: "))
            area = float(pie)*float(r)*float(r)
            print(p_3)
            print('Processing.')
            time.sleep(3)  
            print("The Area of the Circle is:",area)
            print(p_2)
            decision = input("Type Yes For Finding Perimeter else No ")
            if decision.capitalize()=="Yes":
                print(p_2)
                print('Processing.')
                time.sleep(3)  
                print("\nThis is the Circumfernce of Circle",2*pi*r)
                print(p_2)
                print("Thankyou for using Mathematics Game")
                print(p_1)
            elif decision.capitalize()=="No":
                print(p_1)
                print("Thankyou for using Mathematics Game")
                print(p_1)
    
            else :
                print(p_1)
                print ("invalid input")
                print("Thankyou for using Mathematics Game")
                print(p_1)

#This is for finding Paralellogram related values---(CCJustCodingWithVivek)
    if choice==5:
        print("You Entered and Finding Paralellogram Related Values")
        print(p_1)
        l=int(input("Enter the length: "))
        b=int(input("Enter the breadth: "))
        print(p_3)
        print('Processing.')
        time.sleep(3)  
        print("\nThis the Area of Paralellogram: ",l*b)
        print(p_2)
        decision = input("Type Yes For Finding Perimeter else No ")
        if decision.capitalize()=="Yes": 
            print(p_2)
            print('Processing.')
            time.sleep(3)  
            print("\nThis is the Perimeter of Paralellogram: ",2*(l+b))
            print(p_2)
            print("Thankyou for using Mathematics Game")
            print(p_1)
        else:
            print(p_1)
            print("Thankyou for using Mathematics Game")
            print(p_1)

#This is for finding Trapezium related values---(CCJustCodingWithVivek)
    if choice==6:
        print("You Entered and Finding Trapezium Related Values")
        print(p_1)
        a=int(input("Enter the 1st Side: "))
        b=int(input("Enter the 2nd Side: "))
        h=int(input("Enter the height: "))
        print(p_3)
        print('Processing.')
        time.sleep(3)  
        print("\nThis the Area of Trapezium: ",a+b/2*h )
        print(p_2)
        decision = input("Type Yes For Finding Perimeter else No ")
        if decision.capitalize()=="Yes":
            print(p_3)
            c=int(input("Enter the 3rd Side: "))
            d=int(input("Enter the 4th Side: ")) 
            print(p_3)  
            print('Processing.')
            time.sleep(3)  
            print("\nThis is the Perimeter of Trapezium: ",a+b+c+d)
            print(p_2)
            print("Thankyou for using Mathematics Game")
            print(p_1)
        else:
            print(p_1)
            print("Thankyou for using Mathematics Game")
            print(p_1)

#This is for finding Rhombus related values---(CCJustCodingWithVivek)
    if choice==7:
        print("You Entered and Finding Rhombus Related Values")
        print(p_1)
        d1=int(input("Enter the 1st diagonal length: "))
        d2=int(input("Enter the 2nd diagonal length: "))
        print(p_3)
        print('Processing.')
        time.sleep(3)  
        print("\nThis the Area of Rhombus: ",d1*d2/2 )
        print(p_2)
        decision = input("Type Yes For Finding Perimeter else No ")
        if decision.capitalize()=="Yes":
            print(p_3)
            s=int(input("Enter the Side Length: "))  
            print(p_3) 
            print('Processing.')
            time.sleep(3)  
            print("\nThis is the Perimeter of Rhombus: ",s*4)
            print(p_2)
            print("Thankyou for using Mathematics Game")
            print(p_1)
        else:
            print(p_1)
            print("Thankyou for using Mathematics Game")
            print(p_1)

#This is for finding Rhombus related values---(CCJustCodingWithVivek)
    if choice==8:
        print("You Entered and Finding Kite Related Values")
        print(p_1)
        d1=int(input("Enter the 1st diagonal length: "))
        d2=int(input("Enter the 2nd diagonal length: "))
        print(p_3)
        print('Processing.')
        time.sleep(3)  
        print("\nThis the Area of Kite: ",d1*d2/2 )
        print(p_2)
        decision = input("Type Yes For Finding Perimeter else No ")
        if decision.capitalize()=="Yes":
            print(p_3)
            s=int(input("Enter the 1st Side Length: "))
            p=int(input("Enter the 2nd Side Length: "))
            print(p_3)   
            print('Processing.')
            time.sleep(3)  
            print("\nThis is the Perimeter of Kite: ",2*(s+p))
            print(p_2)
            print("Thankyou for using Mathematics Game")
            print(p_1)
        else:
            print(p_1)
            print("Thankyou for using Mathematics Game")
            print(p_1)

    elif choice>=9:
        print(p_1)
        print("""Invalid input!!!
        Next time Put Proper values""")
        print(p_1)

    m1=input("Press Yes to continue or Press any other button to exit: ")
    if m1.capitalize()=="Yes":
        continue
    else:
        break
