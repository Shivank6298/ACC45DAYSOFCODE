

def printinfo(arg1,*vartuple ):
    print("output is : ")
    print(arg1)
    sum=0
    for var in vartuple :
        sum=sum+var
    per=sum/5
    print("the percentage is: ",per)
    return
    
printinfo(10,12,13,14)
    

    