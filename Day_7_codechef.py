#Chef has to travel to another place. For this, he can avail any one of two cab services.

#The first cab service charges XX rupees.
#The second cab service charges YY rupees.

t=0
x=int(input("enter the price"))
y=int(input("enter the second price"))

if x==y:
    print("take any")
    t=t+1
elif x<y:
    print("take first ")
    t=t+1
else :
    
    print("take second ")
    t=t+1

