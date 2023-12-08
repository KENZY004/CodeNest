#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kenzn
#
# Created:     29-09-2023
# Copyright:   (c) kenzn 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
digits=[]
sum1=0
temp=0
num=int(input("n: "))
temp=num
while(temp!=0):
    digits.append(temp%10)
    temp=temp//10
power=len(digits)
for x in digits:
    sum1=sum1+ x ** power
print("sum of powers:",sum1)
if(sum1==number):
    print("armstrong number")
else:
    print("not armstrong number")
