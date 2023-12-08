#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      kenzn
#
# Created:     30-10-2023
# Copyright:   (c) kenzn 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

list1=input(" ").split(",")
print(list1)
list2=input(" ").split(",")
list1.append(list2)
print("after append:",list1)
data3=input(" ").split(",")
list1.append(data3)
print("after appending:",list1)
list1.extend(data3)

