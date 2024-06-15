#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      deepa
#
# Created:     16-06-2024
# Copyright:   (c) deepa 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#Question 23
# Write a program that converts temperature from Celsius to Fahrenheit
# and vice versa based on user input.
def cel(temp):
    #F-->C
    Temp=(temp-32)*(5/9)
    print("The temperature in Celsius is",int(Temp),"degree C")
def fah(temp):
    #C --> F
    Temp= (9/5)*temp+32
    print("The temperature in Fahrenheit is",int(Temp),"degree F")

n=int(input("Enter the temperature: "))
p=input("Enter the unit(F/C): ")
if p.upper()=="F":
    cel(n)
if p.upper()=="C":
    fah(n)

# Question 24
# Write a program that acts as a simple calculator. It should take two
# numbers and an operator (+, -, *, /) as input and print the result.
def calc(s1,s2):
    n=input("ENter the operand: ")
    if n=='+':
        print("The sum is:",s1+s2)
    elif n=="-":
        if s1>s2:
            print("The difference is:",s1-s2)
        else:
            print("The difference is",s2-s1)
    elif n=="*":
        print("The product is:",s1*s2)
    else:
        if s1>s2 and s2!=0:
            print("The quotient is:",s1/s2)
        elif s1>s2 and s2==0:
            print("undefined")
        elif s2>s1 and s1!=0:
            print("The quotient is:",s2/s1)
        else:
            print("undefined")
s1=int(input("Enter 1st number: "))
s2=int(input("Enter 2nd number: "))
calc(s1,s2)

# Question 25
#  Write a program that copies the contents of one text file to another
with open('first.txt','r') as firstfile, open('second.txt','a') as secondfile:

    for line in firstfile:
             secondfile.write(line)

# Question 26
# Write a program in python that checks if a string starts with a given prefix
# or ends with a given suffix.
n=input("Enter the prefix: ")
m=input("Enter the suffix: ")
print(str.startswith(n))
print("\n")
print(str.endswith(m))

# Question 27
# Write a program in python that converts a string into a list of its characters.
n=input("Enter a string: ")
l=[]
for i in n:
    l.append(n)
print("The list of characters of the given string is: ",l)
