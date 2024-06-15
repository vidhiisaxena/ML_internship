#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      deepa
#
# Created:     15-06-2024
# Copyright:   (c) deepa 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#Question 12
# Write a python program that calculates the sum of the digits of a given
# number
n=int(input("Enter the number: "))
count=0
for i in range(0,n+1):
    count+=i
print("The sum of digits of the given number is: ",count)


#Question 13
# Write a program that asks the user for their birth year and calculates their
# age
import datetime
n=int(input("Enter your birth year: "))
today=datetime.date.today()
age=today.year-n
print("Your age is",age,"years old")


#Question 14
# Write a program that reads multiple lines of input from the user until they
# enter an empty line, then prints all the lines
def txt():
    n=input("Enter text: ")
    if len(n)==0:
        print("")
    else:
        n=input("Enter text: ")
txt()


#Question 15
# Write a program that reads data from a CSV file and prints it to the
# console
import csv
fields=["Name", "Branch", "Year"]
rows=[["Aasha","CSE","2026"],["Niya","ECE", "2027"]]
filename="records.csv"
with open(filename,"w") as csvfile:
    csvwriter= csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

with open("records.csv", mode='r') as file:
    csv_reader=csv.DictReader(file)
    l=[]
    for rows in csv_reader:
        l.append(rows)
for data in l:
    print(data)


# Question 16
# Write a program in python that counts the frequency of each character in
# a string
string = input("Enter a string: ")
dict = {}

for i in string:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)


# Question 17
# Write a program in python that converts a given string to title case (first
# letter of each word capitalized).
string=input("Enter a string: ")
a=string.capitalize()
print(a)


# Question 18
# Write a python program that checks if two strings are anagrams of each
# other
def anagram(s1,s2):
    if (sorted(s1)==sorted(s2)):
        print("The strings are anagrams")
    else:
        print("The strings aren't anagrams")
s1=input("Enter first string: ")
s2=input("Enter second string: ")
anagram(s1,s2)


# Question 19
# Write a python program that removes all punctuation from a given string.
n=input("Enter a string: ")
l=""
punctuations = "!()-[]{};:'"\,<>../?@#$%^&*_~"
for i in n:
    if i not in punctuations:
        l=l+i
print(str(l))


# Question 20
# Write a python program that takes a list of numbers and returns their sum.
n=int(input("Enter the number of list items: "))
sum=0
for i in range(0,n):
    p=int(input("Enter the number: "))
    sum+=p
print("The sum of the numbers is: ",sum)


# Question 21
# Write a python program that counts the occurrences of a specific element
# in a list.
n=input("Number of elements in the list: ")
l=[]
count=0
for i in range(0,n):
    p=input("Enter the elements: ")
    l.append(p)
m=input("Element to be searched: ")
for i in range(0,len(l)):
    if l[i]==m:
        count+=1
print("The occurrence of the element is: ",count)


# Question 22
# Write a python program that returns the minimum and maximum values
# in a list of numbers.
n=int(input("Enter the number of elements:"))
l=[]
a=0
b=1000000
for i in range (0,n):
    p=int(input("Enter the elements: "))
    l.append(p)
for i in range (0,len(l)):
    if l[i]>a:
        a=l[i]
    if l[i]<b:
        b=l[i]

print("The maximum value is",a,"and the minimum value is",b)




