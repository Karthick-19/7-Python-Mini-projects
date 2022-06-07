#python mini projects
#Karthick-19
#Number guessing game
import random

name=input("Enter your name :")
score = 0
wg=0
#To set a range by user
setr=input("Set a range "+name+" :")
#check setted range and setting it as integer
if setr.isdigit():
    setr=int(setr)
    if setr<=0:
        print("Please enter a number greater than 0")
        quit()
else:
    print("Please type a number")
    quit()

#Checks user guess matches random number
while True:
    #Generating random number
    r=random.randint(0,setr)
    #Makes user guess
    userg=input("Make your guess :")
    #set user guess as integer if not display message
    if userg.isdigit():
        userg=int(userg)
    else:
        print("Make your guess as number!!!")
        continue
    
    if userg==r:
        print("Yaay You got it right")
        score=score+1
        con=input("U wanna continue? ")
        if con.lower() != "yes":
            print("Total score:"+str(score)+"Wrong Attempts:"+str(wg))
            break
        else:
            continue
    else:
        print("Wrong...\nDon't worry try Again")
        wg+=1
