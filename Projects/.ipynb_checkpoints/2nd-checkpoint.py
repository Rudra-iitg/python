 # **************************String**************************
str1 = "Hello"
str2 = 'World'
str3 = '''Hello World'''
str4 = """Hello World"""
str5 = "this is first line. \nThis is second line"

# **************************Concatenation**************************

print (str1 + str2)

print(str1)
print(str2)
print(str3)
print(str4)
print(str5)

# **************************length of string**************************

length1 = len(str1)
length2 = len(str2)
length3 = len(str1 + str2)
print (length1)
print (length2)
print (length3)

# **************************Indexing**************************

str6 = "String Checking"
print (str6[7])
#     or
print (str6[-7]) # Negative indexing i.e. it will count from last
#    or
print (str6[0:9]) # Slicing i.e. it will print from 0 to 8
#    or
print (str6[0:]) # It will print from 0 to end
#    or
print (str6[:9]) # It will print from start to 8

# ***************************String Functions**************************

print (str5.endswith("line")) # True
print (str5.startswith("This")) # True
print (str5.find("line")) # 17 i.e. it will return the index of first occurence of "line"
print (str5.count("line")) # 2 i.e. it will return the count of "line"
print (str5.capitalize()) # It will capitalize the first letter of first word
print (str5.upper()) # It will convert the whole string to upper case
print (str5.lower()) # It will convert the whole string to lower case
print (str5.replace("this","That")) # It will replace This with That
print (str5.split()) # It will split the string into words
print (str5.split("i")) # It will split the string with i
print (str5.strip()) # It will remove the leading and trailing spaces
print (str5.lstrip()) # It will remove the leading spaces
print (str5.rstrip()) # It will remove the trailing spaces
print (str5.isalnum()) # False i.e. it will return True if all the characters are alphanumeric
print (str5.isalpha()) # False i.e. it will return True if all the characters are alphabets
print (str5.isdigit()) # False i.e. it will return True if all the characters are digits
print (str5.islower()) # True i.e. it will return True if all the characters are in lower case
print (str5.isupper()) # False i.e. it will return True if all the characters are in upper case 
print (str5.isspace()) # False i.e. it will return True if all the characters are spaces


# ***************************Practice1**************************

# name = input("Enter your first name: ")
# print(len(name))
# print(name.count("q")) 

# ***************************Practice end**************************

# ***************************Conditional Statements**************************

age = int(input("Enter your age: "))

if (age >= 25):
    print("You are eligible for voting")
elif (age <= 18):
    print("You are are kiddow just get out")
else:
    print("You are not eligible for voting")

# ***************************Practice2**************************

number = int(input("Enter a number: "))
if (number % 2 == 0):
    print("Even")
else:
    print("Odd")

# ***************************Practice2**************************

a = int (input("Enter number A: "))
b = int (input("Enter number B: "))
c = int (input("Enter number C: "))

if (a > b and a > c):
    print("A is greater")
elif (b > a and b > c):
    print("B is greater")
else:
    print("C is greater")

# ***************************Practice3**************************

y = int(input("Enter the number: "))
if(y % 7 == 0):
    print(f"{y} is Divisible by 7")
else:
    print(f"{y} is divisible by 7")