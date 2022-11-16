import re

nameage ='''
Janice is 22 and Theon is 33
Gabriel is 44 and Joey is 21'''

ages=re.findall(r'[0-9]+',nameage)
names =re.findall(r'[A-Z][a-z]',nameage)

print(ages)
ageDict={}
x=0
for eachname in names:
    ageDict[eachname]=ages[x]
    x+=1
print(ageDict)