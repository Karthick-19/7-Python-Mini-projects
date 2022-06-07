#python mini projects
#Karthick-19
#Quiz game enter questions accordingly
print("My First Python Program....!!!")

print("PYTHON QUIZ game")

playing = input("Do you want to play the game? ")
if playing.lower() != "yes": #.lower() method is used to convert all text into lowercase text
    quit()

print("OKAYYY Lets playyyy..;)"

score=0

ans=input("What is the result of 99+98? ")
if ans=="197":
    print("BOOM..!Correct Answer")
    score+=1
else:
    print("Incorrect answer try again")

ans=input("Name the alphabet next to j: ")
if ans=="K":
    print("BOOM..!Correct Answer")
    score+=1
else:
    print("Incorrect answer try again")

ans=input("How many shoes Rocky bhai need to clean to get a single bun? ")
if ans=="8":
    print("BOOM..!Correct Answer")
    score+=1
else:
    print("Incorrect answer try again")

ans=input("How many years refers a decade? ")
if ans=="10":
    print("BOOM..!Correct Answer")
    score+=1
else:
    print("Incorrect answer try again")

print("You got "+str(score)+" correct ansers")

