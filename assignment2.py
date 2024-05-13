# n = int(input("Enter any number:"))
# if(n>=0):
#     print(n,"is Positive number.")
# else:
#     print(n,"is Negative number.")

# n = int(input("Enter any number:"))
# if(n%5==0):
#     print(n,"is Divisible by 5.")
# else:
#     print(n,"is not Divisible by 5.")

# n = int(input("Enter any number:"))
# x = int(n/2)*2
# if(x==n):
#     print(n,"is Even number.")
# else:
#     print(n,"is Odd number.")

# n = int(input("Enter any number:"))
# if(n<10):
#     print(n,"is one digit number.")
# elif(n>10 and n<100):
#     print(n,"is two digit number.")
# elif(n>99 and n<1000):
#     print(n,"is three digit number.")
# elif(n>999 and n<10000):
#     print(n,"is four digit number.")
# else:
#     print("Invalid number.")

# a = int(input("Enter 1st number:"))
# b = int(input("Enter 2nd number:"))

# if(a>b):
#     print(a,"is greater than ",b)
# elif(a<b):
#     print(a,"is smaller than ",b)
# elif(a==b):
#     print(a,"Both are same")
# else:
#     print("Sorry, Invalid number")

# n = int(input("Enter the year:"))
# if(n%400==0):
#     print(n," year is leap year.")
# else:
#     print(n," year is not leap year,")

# a = int(input("Enter 1st number:"))
# b = int(input("Enter 2nd number:"))
# c = int(input("Enter 3rd number:"))
# if(a>=b and a>=c):
#     print(a," is Greater.")
# elif(b>=a and b>=c):
#     print(b," is Greater.")
# elif(c>=a and c>=b):
#     print(c," is Greater.")
# else:
#     print("Invalid Number.")

# cp = int(input("Enter the cost price:"))
# sp = int(input("Enter the selling price:"))
# if(sp>cp):
#     profit = (sp-cp)/100
#     print("You profit ",profit," % rupees.")
# elif(cp>sp):
#     loss = (sp-cp)/100
#     print("You loss",loss," % rupees.")
# elif(sp==cp):
#     print("No profit No loss")

# m1 = int(input("Enter the marks of Hindi:"))
# m2 = int(input("Enter the marks of English:"))
# m3 = int(input("Enter the marks of Maths:"))
# m4 = int(input("Enter the marks of Science:"))
# m5 = int(input("Enter the marks of So-science:"))

# total = m1+m2+m3+m4+m5
# avg = total*100/5
# if(avg>=33):
#     print("You are Passed.")
# else:
#     print("You are Fail.")

# ch = input("Enter any alphabet:")
# if(ch>='A' and ch<='Z'):
#      print("You enter uppercase character.")
# else:
#     print("You enter lowercase character.")

# n = int(input("Enter any number:"))
# if(n%3==0 and n%2==0):
#     print(n," is Divisible by 3 and Divisible by 2")

# else:
#     print("It is not Divisible by 2 and 3.")

# n = int(input("Enter any number:"))
# if(n%7==0):
#     print(n," is divisible by 7.")
# elif(n%3==0):
#     print(n," is divisible by 3")
# else:
#     print(n," is not divisible by 7 or 3.")

# n = int(input("Enter any number:"))
# if(n>0):
#     print(n," is positive number.")
# elif(n<0):
#     print(n," is negative number.")
# elif(n==0):
#     print(n," is Zero number.")
# else:
#     print(n," sorry,you enter invalid number.")

# n = str(input("Enter any character:"))
# if(n >= 'A' and n <= 'Z'):
#     print(n," is uppercase alphabet.")
# elif(n>='0' and n<='9'):
#     print(n," is a digit.")
# elif(n >= 'a' and n <= 'z'):
#     print(n," is lowercase alphabet.")
# else:
#     print(n," is special character.")

# a = int(input("Enter the 1st size of triange:"))
# b = int(input("Enter the 2nd size of triangle:"))
# c = int(input("Enter the 3rd size of triangle:"))

# if(a+b>c and a+c>b and b+c>a):
#     print("it is valid triangle.")
# else:
#     print("it is not valid triangle.")

n = int(input("Enter any months:"))
if(n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12):
    print(n," in this month 31 days.")
elif(n==4 or n==6 or n==9 or n==11):
    print(n," in this month 30 days.")
elif(n==2):
    print(n," in this month 28 or 29 days.")