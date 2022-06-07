#python mini projects
#Karthick-19
#Rock paper scissor game
import random#importing random
#declaring variables for userPoints and Computer Points
userp=0
computerp=0
#Available Choices to make
options=["rock","paper","scissor"]

while True:
#Selecting User Choice
    user_choice=input("Rock \nPaper \nScissor \nQ to quit game \nMake your choice: " ).lower()
    if user_choice=="q":#condition for quitting game
        break
    if user_choice not in options:#Checking entered choice
        print("Enter Valid choice")
        continue

    rand=random.randint(0,2)#Generating random number to select computer choice
    computer_choice=options[rand]#Fixing the randomly generated number acc to choice

    print("Computer choice: "+computer_choice)
#Conditions for Wins and Loss 
    if user_choice==computer_choice:
        print("Match draw!!")
        continue
    elif user_choice=="rock" and computer_choice=="scissor":
        print("User Won")
        userp+=1
        continue
    elif user_choice=="paper" and computer_choice=="rock":
        print("User Won")
        userp+=1
        continue
    elif user_choice=="scissor" and computer_choice=="paper":
        print("User Won")
        userp+=1
        continue
    else:
        print("Computer Won")
        computerp=1
        continue
#once control comes out of loop it display user and computer score
print("User Score:",userp)
print("Computer Score:",computerp)
