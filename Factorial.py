#python mini projects
#Karthick-19
while True:
    num=int(input("Enter a number: "))
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
    end=input("Q to quit\nReturn to continue")
    if end=="q":
        break
    

