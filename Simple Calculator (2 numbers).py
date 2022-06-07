#python mini projects
#Karthick-19
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
def addition(num1,num2):
    return num1+num2
def subtraction(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2
while True:
    select=int(input("Select the operation\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n"))
    if select==1:
        print(addition(num1,num2))
    elif select==2:
        print(subtraction(num1,num2))
    elif select==3:
        print(multiply(num1,num2))
    elif select==4:
        print(division(num1,num2))
    else:
        print("Invalid Input")

    qt=input("Q to quit: \nReturn to continue")
    if qt=="q":
        break
    else:
        continue
