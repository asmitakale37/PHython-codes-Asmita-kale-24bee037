#Fliter even and odds from the list
from functools import reduce
num=[1,2,3,4,5,7,8,9,10,11,12,14,15,16]
evens=list(filter(lambda n:n%2==0,num))
print(evens)
#square
square=list(map(lambda n:n*n,num))
print(square)
#sum
sum=reduce(lambda a,b:a+b,square)
print(sum)
#5
names=["asmitakale","rakeshkale","het","aayan","nilesh","jelam"]
name=list(filter(lambda n:len(n)>8,names))
print(name)
#3
num=[1,2,3,5,4,-1,-2,-3,-4,-11]
square=list(map(lambda n:n*n,num))
print(square)
#2
num1=[1,2,3,4,5,6]
num2=[6,5,4,3,2,1]
sums=list(map(lambda a,b:a+b,num1,num2))
print(sums)
#4
lst=['madam','phython',"malayalan",123321]
palindromes=list(filter(lambda s:str(s)==str(s)[::-1],lst))
print(palindromes)
#1
def fun():
    print("This is the function fun()")
def disp():
    print("This is the function disp()")
def msg():
    print("This is the function msg()")
functions=[fun,disp,msg]
for func in functions:
        func()

