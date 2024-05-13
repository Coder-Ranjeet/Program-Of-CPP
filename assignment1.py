# n = int(input("Enter any number:"))
# b = n%10
# print(b," is the unit digit.")

# n = int(input("Enter any number:"))
# b = n//10
# # c = b%10
# print(b," number without last digit.")

# a = int(input("Enter 1st number:"))
# b = int(input("Enter 2nd number:"))
# temp = a
# a = b
# b = temp
# print("swapping number is: ",a,b)

# a = int(input("Enter 1st number:"))
# b = int(input("Enter 2nd number:"))
# a = a+b
# b = a-b
# a = a-b
# print("swapping value is: ",a,b)

# n = int(input("Enter three digit-number:"))
# a = n%10  #last digit
# d = n//10 #1st and 2nd digit
# b = d%10  #middle digit
# c = n//100 #1st digit
# print(a+b+c)
# print(d)

# n = str(input("Enter any character:"))
# print("the ascii value of",n,"is",ord(n))

# n = int(input("Enter any number:"))
# lsb = (n & 1)
# print(lsb)

# n = int(input("Enter any number:"))
# if(n&1==0):
#   print(n," is even number.")
# else:
#   print(n," is odd number.")

# import sys

# def print_size_of_data_types():
#     # Size of int
#     print("Size of int:", sys.getsizeof(int()))

#     # Size of float
#     print("Size of float:", sys.getsizeof(float()))

#     # Size of character (technically, there's no character data type in Python; using a string of length 1)
#     print("Size of character:", sys.getsizeof('a'))

#     # Size of double (In Python, there's no distinction between float and double; both are represented as float)
#     print("Size of double:", sys.getsizeof(float()))

# print_size_of_data_types()

# n = int(input("Enter the number:"))
# a = n//10
# b = a*10
# print(b)

# n = int(input("Enter the number:"))
# digit = int(input("Enter digit:"))
# # number = n//10
# result = int(str(n) + str(digit))
# print(result)

# usd = 0.012  #1 dollar = 83.38
# rupee = float(input("Enter the rupee:"))
# dollar = rupee*usd
# print(dollar)

# number = int(input("Enter the integer number: "))  
  
# revs_number = 0  
  
# while (number > 0):  
#     remainder = number % 10  
#     revs_number = (revs_number * 10) + remainder  
#     number = number // 10  
  
# print("The reverse number is :",revs_number) 

