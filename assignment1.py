# This program print last digit of a number e.g- input 123,output 3
n = int(input("Enter any number:"))
b = n%10
print(b," is the unit digit.")

#This program print middle integer e.g- input 523,output 2
n = int(input("Enter any number:"))
b = n//10
c = b%10
print(c," number without last and first digit.")

#Swapping two number by using third variable e.g- input 32,output 23
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
temp = a
a = b
b = temp
print("swapping number is: ",a,b)

#Swapping two number without using third variable e.g- input 54,output 45
 a = int(input("Enter 1st number:"))
 b = int(input("Enter 2nd number:"))
 a = a+b
 b = a-b
 a = a-b
 print("swapping value is: ",a,b)

#This program print sum of three digit and print without last digit e.g- input 523,output 10 and 52
 n = int(input("Enter three digit-number:"))
 a = n%10  #last digit
 d = n//10 #1st and 2nd digit
 b = d%10  #middle digit
 c = n//100 #1st digit
 print(a+b+c)
 print(d)

#This program print ascii value input by the user e.g- input b, output 98
 n = str(input("Enter any character:"))
 print("the ascii value of",n,"is",ord(n))

#This program print the least segnificant bit e.g- input 5,output 1 and input 4,output 0 and input 1,output 1
n = int(input("Enter any number:"))
lsb = (n & 1)
print(lsb)

#This program print even/odd number without using modulus operator.
n = int(input("Enter any number:"))
if(n&1==0):
  print(n," is even number.")
else:
  print(n," is odd number.")

#This program print the size of datatype.
import sys
def print_size_of_data_types():
    # Size of int
    print("Size of int:", sys.getsizeof(int()))
    # Size of float
    print("Size of float:", sys.getsizeof(float()))
    # Size of character (technically, there's no character data type in Python; using a string of length 1)
    print("Size of character:", sys.getsizeof('a'))
    # Size of double (In Python, there's no distinction between float and double; both are represented as float)
    print("Size of double:", sys.getsizeof(float()))
print_size_of_data_types()

#This program print the multiple of 10 with flour digit e.g- input 256,output 250. how see flour digit of 256 is 25 and 25*10=250 
n = int(input("Enter the number:"))
a = n//10
b = a*10
print(b)

#This program print the number and add extra number in last last of the number. e.g- input 123,4 and output 1234
n = int(input("Enter the number:"))
digit = int(input("Enter digit:"))
# number = n//10
result = int(str(n) + str(digit))
print(result)

#This program convert the indian rupees to american dollar.
usd = 0.012  #1 dollar = 83.38
rupee = float(input("Enter the rupee:"))
dollar = rupee*usd
print(dollar)

#This program print the reverse number. e.g- input 1234 and output 4321
number = int(input("Enter the integer number: "))   
revs_number = 0   
while (number > 0):  
    remainder = number % 10  
    revs_number = (revs_number * 10) + remainder  
    number = number // 10  
print("The reverse number is :",revs_number) 

