name=input("Text")
rev=name[::-1]
print(rev)
if(name==rev):
  print("pallindrome")
else:
    print("Not pallindrome")

#Count how many vowels are there in a string.Accept the string from the user
f=input("Enter the string")
v=0
for i in f:
    if(f[i]="a",f[i]="e",f[i]="i",f[i]="o",f[1]="u")
      v=v+1
print("number of string=",v)
     else:
         print("Processing")
         

#Accpet the two strings .check whether one string is in another string
str1="I AM IN PDPU"
str2="HI HELLO PDPU"
if ("PDPU"in str2):
         print("String is present")
else:
         print("Not")
#Write a function That Removes one string from another string
string="abcdef"
for x in string
x.in.replace("abef")

#LAB4

#Write a program for for the first n  natural number sum.
num=int(input("n"))
total=0
for i in range(1,7):
    total=total+num
    num=num+1
print(total)

#Write a program for the factorial
r=1
n=int(input("n"))
while(n!=0):
  r=r*n
  n=n-1
print(r)

#Write a table of a number
num=int(input("Number"))
for i in range(1,11):
    result=num*i
    print(f"{num}*{i}={result}")
# Print the  table from 1 to 10
num=0
for j in range(1,11):
   for i in range(1,11):
     result=i*j
     print(result)

#Check whether the given number is prime or not
num=int(input("Number"))
if(num/3==1):
  print("It is  prime")
elif(num/5==1):
  print("It is  prime")
elif(num/7==1):
  print("It is  prime")
else:
    print(" Not Prime")

#Print all alphabets in Upper case and lower case
# Printing uppercase alphabets
print("Uppercase Alphabets:")
for i in range(65, 91):
    print(chr(i), end=' ')
print()

# Printing lowercase alphabets
print("Lowercase Alphabets:")
for i in range(97, 123):
    print(chr(i), end=' ')
print()
#Check whether the given number is palindrome or not
S=int(input("Number"))
S[::-1]

# Generate N numbers of Fibonacci series using a loop

# Input: Number of Fibonacci numbers to generate
N = int(input("Enter the number of Fibonacci numbers to generate: "))

# First two Fibonacci numbers
a, b = 0, 1

print("Fibonacci Series:")

for i in range(N):
    print(a, end=" ")
    a, b = b, a + b

 


