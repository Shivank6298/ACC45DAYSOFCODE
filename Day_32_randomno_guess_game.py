#random guess game
import random
attempts=4

computer_no=random.randrange(1,10)
while attempts>0:
    n=int(input("enter the no."))
    if n==computer_no:
        print("you win")
        break;
    else:
        print("you lose , try again")
        attempts=attempts-1