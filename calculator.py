#copyright @Satwik Kaushik
import math
from math import sqrt
while True:
#welcoming the user
    print("                                                  Welcome")
    user_input=input("Which calculation should we do?")
    if user_input=="quit":
        break
#for addition
    elif user_input=="add" or user_input=="addition" or user_input=="sum" or user_input=="+":
        num1=float(input("First Number:"))
        num2=float(input("Second Number"))
        result=str(num1+num2)
        print(result)
#for subtraction
    elif user_input=="sub" or user_input=="subtract" or user_input=="substraction" or user_input=="difference" or user_input=="-":
        num1=float(input("First Number"))
        num2=float(input("Second Number"))
        result=str(num1-num2)
        print(result)
#for multiplication
    elif user_input=="mul" or user_input=="multiply" or user_input=="multiplication" or user_input=="*" or user_input=="x":
        num1 = float(input("First Number"))
        num2 = float(input("Second Number"))
        result = str(num1 * num2)
        print(result)
#for division
    elif user_input=="div" or user_input=="divide" or user_input=="division" or user_input=="/":
        num1 = float(input("First Number"))
        num2 = float(input("Second Number"))
        result = str(num1 / num2)
        print(result)
#for power
    elif user_input=="power" or user_input=="find the power" or user_input=="^":
        num1=float(input("Number:"))
        num2=float(input("To the power of:"))
        result=str(num1**num2)
        print(result)
#for root
    elif user_input=="square root" or user_input=="root":
        num=float(input("Enter the number:"))
        result=str(sqrt(num))
        print(result)
#for force
    elif user_input=="force" or user_input=="force applied" or user_input=="F":
        mass = float(input("Mass:"))
        accleration = float(input("Accleration:"))
        result = str(mass * accleration)
        print(result + "N")
#for momentum
   elif user_input=="momentum" or user_input=="P":
        mass=float(input("Mass:"))
        velocity=float(input("Velocity:"))
        result=mass*velocity
        print(result + "kg m/s")
#for else statements
    else:
        print("UNKNOWN INPUT")
    break
#end
