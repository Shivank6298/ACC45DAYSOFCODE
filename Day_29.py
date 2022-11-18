

def printinfo(arg1,*vartuple ):
    print("output is : ")
    print(arg1)

    for var in vartuple:
        print(var)
    return

printinfo(10)
printinfo(170,50,80)
printinfo(10,11,12,13,14)