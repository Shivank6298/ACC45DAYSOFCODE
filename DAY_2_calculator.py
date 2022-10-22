
while True:
    print("1. ADDITION ")
    print("2. SUBSTRACTION ")
    print("3. MULTIPLICATION ")
    print("4. DIVISION ")
    print("5. EXIT ")
    print(" ENTER YOUR CHOICE(1-5):",end="")
    ch=int(input())
    if ch>=1 and ch<=4:
        print("enter two numbers:")
        numone=float(input())
        numtwo=float(input())
    if ch==1:
        res=numone+numtwo
        print("\n result =",res)
    elif ch==2:
        sub=numone-numtwo
        print("\n result =",sub)
    elif ch==3:
        mul=numone*numtwo
        print("\n result =",mul)
    elif ch==4:
        div=numone/numtwo
        print("\n result =",div)
    elif ch==5:
        break;
    else:
        print("\n invalid input try again")

print("----------/---------/-----/----/---/")
