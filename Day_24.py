#Our Chef took the above advice very seriously and decided to set a target for himself.

#Chef decides to solve at least 1010 problems every week for 44 weeks.
#Given the number of problems he actually solved in each week over 44 weeks as P_1, P_2, P_3,P4, output the number of weeks in which Chef met his target


arr=list(map(int,input().split()))
a=0
for i in range(4):
    if arr[i]>=10:
        a+=1
print(a)