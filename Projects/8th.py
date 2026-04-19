# **************************Recursions**************************
# Recursion is a method where the solution to a problem depends on solutions to smaller instances of the same problem.
# Recursions are used to solve problems that contain smaller sub-problems.
# When function calls itself repetedly, it is called recursion.
"""n = 5
def show(n):
    print(n)
    show(n-1)
show(n)"""
# This will run infinitely because we have not defined any base case.
# A base case is a condition that stops the recursion.
# To stop the recursion, we need to define a base case.

n = 5
def show(n):
    if n == 1:
        return 1
    print(n)
    show(n-1)
show(n)
# This will print 5 4 3 2 1
# The base case is n == 1
# The function will keep calling itself until n == 1
# The function will print n and then call itself with n-1
# The function will keep calling itself until the base case is met.
f = 6
def fact(f):
    if (f == 1):
        return 1
    return f * fact(f-1)
print(fact(f))  
# **************************Practice1**************************
# Write a recursive function to calculate the sum of first n natural numbers.
x = 10
def sum(x):
    if (x == 1):
        return 1
    return x + sum(x-1)
print(sum(x))