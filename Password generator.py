#Password generator
#python mini projects
#Karthick-19import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
number = "1234567890"

all= lower+upper+number
length=9

while True:
    password="".join(random.sample(all,length))
    print("The randomly generated password is: ",password)
    rpt=input("Q to quit: ").lower()
    if rpt=="q":
        break
    else:
        continue
        
