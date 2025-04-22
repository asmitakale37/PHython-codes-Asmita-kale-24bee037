a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
print(a)
print(b)
if(a>b):
    print("a is greater")
else:
        print("b is greater")
# Find the greatest number for 3 numbers using if else
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
print(a)
print(b)
print(c)
if(a>b and a>c):
    print("a is greater")
elif(b>c and b>a):
    print("b is greatest")
else:
    print("c is greatest")

#Print largest and Smallest values out of two
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
print(a)
print(b)
if(a>b):
    print("a is greater")
    print("b is smallest")
else:
    print("b is greater")
    print("a is smallest")
# Print largest and smallest values out of three
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
print(a)
print(b)
print(c)
if(a>b and a>c):
    print("a is greater")
    if(b>c):
        print("c is smallest")
    else:
         print("b is smallest")
elif(b>c and b>a):
    print("b is greatest")
    if(c>a):
        print("a is smallest")
    else:
         print("c is smallest")
else:
    print("c is greatest")
    if(a>b):
        print("b is smallest")
    else:
         print("a is smallest")

#Check whether a given number is odd or even
a=int(input("Enter a number:"))
print(a)
if(a%2==0):
  print("EVEN")
else:
      print("ODD")
#Check whether the given number is divisible by 10
a=int(input("Enter a number:"))
print(a)
if(a%10==0):
  print("Divisble by 10")
else:
      print("Not Divisbile by 10")

#Accept age of a person. If age is less than 18, print minor otherwise Major.
a=int(input("Enter age:"))
print(a)
if(a<18):
  print("Minor")
else:
      print("Major")

#Accept a number from the user. And print number of digits in it.
a=input("Enter a number:")
num_digit=len(a)
print("lenght of number",num_digit)

#Accept a year value from the user. Check whether it is a leap year or not.
a=int(input("Enter Year:"))
print(a)
if(a%4==0 and a%100!=0):
    print(" its a Leap year")
else:
    print("its not")

#Check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard. A triangle is valid if te sum of all the three angles is equal to 180 degrees
a=float(input("A"))
b=float(input("B"))
c=float(input("C"))
print(a)
print(b)
print(c)
if(a+b+c==180):
    print("TRIANGLE IS VALID")
else:
    print("TRIANGLE IS NOT VALID")

#Print absolute value of a given number.
a=int(input("Enter a number:"))
print(a)
if(a//1):
    print("IT IS A ABSOLUTE NUMBER")
else:
    print("IT IS NOT")

#Given the length and breadth of a rectangle, write a program to find whether the area of the rectangle is greater than its perimeter
L=float(input("Enter lenght"))
B=float(input("Enter Breath"))
print(L)
print(B)
Area=L*B
print(Area)
Perimeter=2*(L+B)
print(Perimeter)
if(Area>Perimeter):
    print("Area is Greater")
else:
    print("Perimeter is greater")

#Given three points (x1,y1), (x2,y2) and (x3,y3), check if all the three points fall on one straight line.
x1=int(input("x1"))
x2=int(input("x2"))
y1=int(input("y1"))
y2=int(input("y2"))
x3=int(input("x3"))
y3=int(input("y3"))
a= 1/2*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
if(a==0):
    print("IT IS COLLINEAR")
else:
    print("IT IS NOT COLLINEAR")

#Given the coordinates (x,y) of center of a circle and its radius, determine whether a point lies inside the circle, on the circle or outside the circle.
  x1= int(input("x1"))
  y1=int(input("y1"))
  x2= int(input("x2"))
  y2= int(input("y2")
  r=int(input("Enter the radius"))
  pc=(pow(x2-x1,2)+pow(y2-y1,2))
  if(pc>r):
          print("Lies outside the circle")
  else:
      print("Lies Inside the circle")


#13)	Convert number 0 to 19 to its equivalent words. E.g. 0  zero, 19nineteen
    def number_to_words(n):
    words = [
        "zero", "one", "two", "three", "four", "five", 
        "six", "seven", "eight", "nine", "ten", 
        "eleven", "twelve", "thirteen", "fourteen", 
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]
    if 0 <= n <= 19:
        return words[n]
    else:
        return "Number out of range"

#14)	Accept marks of three subjects. Print total and average along with whether a candidate has passed or fail. If student secures <= 39 marks in any subject, consider him as fail. Also assigned a subject wise grade based on the following table:
Marks Range	Grade
Absent	NA
0 – 39	F
40 – 44	P
45 – 49	C
50 – 54	B
55 – 59	B+
60 – 69	A
70 – 79	A+
80 – 100	O

 marks=int(input("Marks"))
 if marks==Absent:
     print("NA")
 elif 0<=marks<=39:
     print("F")
 elif 40<=marks<=44:
     print("P")
 elif 45<=marks<=49:
     print("C")
 elif 50<=marks<=54:
     print("B")
 elif 55<=marks<=59:
     print("B+")
 elif 60<=marks<=69:
     print("A")
 elif 70<=marks<=79:
     print("A+")
 elif 80<=marks<=100:
     print("O")
 else:
     print("INVALID")
     
    

          
  

  
  
