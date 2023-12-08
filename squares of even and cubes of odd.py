#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      kenzn
#
# Created:     02-11-2023
# Copyright:   (c) kenzn 2023
# Licence:     <your licence>
#--------------------------------------------------------
n1=int(input("starting value: "))
n2=int(input("ending value: "))
myset=[i**2 if i %2==0 else i**3 for i in range(n1,n2)]
ss=sorted(myset)
print(ss)
