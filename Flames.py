#python mini projects
#Karthick-19
#Flames
#Get 2 names as input from user store them as list
#compare them and delete the matching letters 
#Get remaining letters and store them in a separate list
#Convert them into Uppercase/Lowercase
#Genrate a list of Flames signs
#Delete sighns according to remaining letter from list
#Display remaining sign
Name1=list(input("Enter 1st name: "))
Name2=list(input("Enter 2nd name: "))
for i in Name1[:]:
    if i in Name2:
        Name1.remove(i)
        Name2.remove(i)
All=Name1+Name2
for i in range(len(All)):
    All[i]=All[i].upper()
game=["Friends","Lovers","Affection","Marriage","Enemies","Siblings"]
count=len(All)
while len(game)>1:
    clc=(count % len(game)-1)
    if clc>=0:
        right=game[clc+1:]
        left=game[:clc]
        game=right+left
    else:
        game=game[:len(game)-1]
print("Relationship Status:",game[0])

