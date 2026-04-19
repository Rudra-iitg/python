print("This is my first python programme")
print("My age is 23 ")
print(25)
print(34+16*10)
name = "Rahul"
age = 23
print(name)
print(age)
print("My name is : ",name)
print("My age is : ",age)
print("My name is : ",name," and my age is : ",age)
age2=age
price = 175.42
truth = True
print(age2)
print(type(age))
print(type(name))
print(type(age2))
print(type(price))
print(type(truth))
a = 10
b =13
sum = a+b
print("Sum of a and b is : ",sum)
# **************This is a comment**************
"""This 
is 
a 
multiline
 comment"""


 #      **************************Arithmetic Operators**************************


# All the + - * /  % are same just as C language
c = 10
d = 3
print(c ** d) # 10^3 = 1000
print(c // d) # 10/3 = 3.3333 so // will give 3
print(c % d) # 10%3 = 1
print(c / d) #10/3 = 3.3333
print(c + d) # 10+3 = 13
print(c - d) # 10-3 = 7

#      ************************** Relational / Comparison Operators**************************

x = 25
y = 30
print(x == y) # False
print(x != y) # True
print(x>=y) # False
print(x<=y) # True


#      ************************** Assignment Operators**************************

num = 10
#num = num + 10
num += 10
print(num) # 20
# similar for  + - * / % // **

#      ************************** Logical Operators**************************

print(not True) # False
print(not(a>b)) # True
val1 = True
val2 = False
print(val1 and val2) # False
print(val1 or val2) # True
print((a == b) and (a < b)) # False

# ************************** Type Conversion **************************

p = 45
q = 67.5
print(p+q)# Error
print(type(p))# <class 'int'>

#*******************************Input from user********************************
name = input("Enter your name : ")
print("Your name is : ",name)

#*******************************Practice1********************************

y = int(input("Enter a number : "))
z = int(input("Enter another number : "))
sum = y+z
print("Sum of two numbers is : ",sum)

#*******************************Practice2********************************

side = int(input("Enter the lenth of side : ") )
print("Area of square is : ",side*side)

#*******************************Practice3********************************

num1 = float(input("Enter a number : "))
num2 = float(input("Enter another number : "))
average = (num1+num2)/2
print("Average of two numbers is : ",average)