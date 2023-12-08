#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      kenzn
#
# Created:     27-10-2023
# Copyright:   (c) kenzn 2023
# Licence:     <your licence>
#----------------------------------------------------------------------------
data=input("data: ")
data=[int(x) for x in data.split(",")]
s_e=sum(data)
s=[x**2 for x in data]
s_s=sum(s)
print("list: ",data)
print("sum: ",s_e)
print("squares: ",s)
print("sum of squares:",s_s)