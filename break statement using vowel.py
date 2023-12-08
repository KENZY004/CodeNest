#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kenzn
#
# Created:     27-09-2023
# Copyright:   (c) kenzn 2023
# Licence:     <your licence>
#------------------------------------------------------------------------------
while True:
    input1=input("vowel, or 9 to quit: ")
    if input1.isdigit() and input1!="9":
        print("wrong input")
    elif input1.lower() in "aeiou":
        print("vowel")
    elif input1=="9":
        break
    else:
        print("not vowel")
