#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      deepa
#
# Created:     14-06-2024
# Copyright:   (c) deepa 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#Question 1
#Write a program that takes two numbers as input and prints their sum.
'''
N1= int(input("Enter the first number:"))
N2= int(input("Enter the secind number: "))

sum=N2+N1
print("The sum of the two numbers is: ",sum)

#Question 2
# Write a python program that checks whether a given number is even or odd
N= int(input("Enter the number to be checked: "))
if N%2==0:
    print("It is an even number")
else:
    print("It is an odd number")

#Question 3
# Write a python program that calculates the factorial of a given number
n=int(input("Enter the number whose factorial is to be calculated: "))
x=0
N=n
if N<0:
    print("0")
elif N==0 or N==1:
    print("1")
else:
    f=1
    while(N>1):
        f*=N
        N=N-1
print("The factorial of",n,"is",f)

#Question 4
#Write a program that asks the user for their name and then prints a
#greeting message
Name=input("Enter your name: ")
print("Good Morning",Name)

#QUestion 5
#Write a program that takes a string input from the user and writes it to a
#text file.
String=input("Enter a string: ")
f= open ("string.txt","w")
f.write(String)
f.close()

#Questions 6
#Write a program that reads the content of a text file and prints it to the
#console
f=open("string.txt","r")
print(f.read())
f.close()

#Question 7
#Write a python program that takes a string as input and returns its length
string=input("Enter a string: ")
length=0
for i in range (0,len(string)):
    length+=1
print("The lenght of the string ",string,"is ",length)

#Question 8
#Write a python program that concatenates two strings and returns the
#result
S1=input("Enter string 1: ")
S2=input("Enter string 2: ")
S3= S1+S2
print(S3)

#Question 9
#Write a python program that checks if a substring is present in a given
#string
S1=input("Enter the main string: ")
s=input("Enter the substring: ")
if s in S1:
    print("Substring found")
else:
    print("Substring NOT found")

#Question 10
#Write a python program that converts a given string to uppercase
S=input("Enter a string: ")
n=S.upper()
print(n)
'''
#Question 11
#Write a python program that generates the first n numbers in the
#Fibonacci sequence
n=int(input("Enter the number: "))
num1=0
num2=1
nxt_num= num2
print(num1)
print(num2)
for i in range(0,n-2):
    print(nxt_num,end="\n")
    num1,num2=num2,nxt_num
    nxt_num=num1+num2