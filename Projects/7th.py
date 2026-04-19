# ****************************Functions****************************
from ast import Return


def clacu_sum(a,b):
    sum = a + b
    print("The sum of ", a, " and ", b, " is: ", sum)
    return sum
clacu_sum(5, 6)
clacu_sum(7, 8)
clacu_sum(9, 10)
# **************Or simply**************
def clacu_sum(a,b):
    return a+b
print(clacu_sum(5, 6))
print(clacu_sum(7, 8))  

# ***********************Practice 1**********************
# Write a function to find the average of 3 numbers
def clalc_avg(a,b,c):
    return (a+b+c)/3
print(clalc_avg(5,6,7))
print(clalc_avg(8,9,10))

# ***********************Practice 2**********************
# To print the length of the list
subjects = ["Maths", "Physics", "Chemistry", "Biology", "English"]
food = ["Biryani", "Pulao", "Karahi", "Kabab", "Nihari", "Qorma"]
def print_len(list):
    return len(list)
print(print_len(subjects))
print(print_len(food))
# To print the content of the list in the same line
print(subjects[0] , end= " ")
print(subjects[1], end= " ")

def print_list(list):
    for i in list:
        print(i, end= " ")
print_list(subjects)
print()
print_list(food)
print()

# ***********************Practice 3**********************
# Write a function to print the factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print(factorial(5))
print(factorial(6)) 

# ***********************Practice 4**********************
# Conver USD to INR
# 1 usd = 85INR
def conv_inr(usd):
    return usd*85
print(conv_inr(1) , "INR")
print(conv_inr(5), "INR")

# ***********************Practice 5**********************
# Write a function to print ODD and EVEN form teh given number
def odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(odd_even(5))
print(odd_even(6))