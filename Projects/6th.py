# **************************Ranges***************************
# Ranges are used to generate a sequence of numbers.
# They are immutable (cannot be changed).
# They are used in for loops.
seq = range(10)
print(seq[5])
print(seq[3]) 
for i in seq:
    print(i)
print("NExt")

# **************OR**************
for i in range(12 ):
    print(i)

for X in range(5,12): # range(start, end)
    print(X)

for Y in range(5, 12, 2): # range(start, end, step)
    print(Y)

# ***********************Practice 1**********************
# Print aa number from 1 to 100 using range
for i in range(1,101):
    print(i)

# In reverse order
for j in range(100, 0, -1):
    print(j)

# ***********************Practice 2**********************
# Print a multiple table of a number n using for loop
#n = int(input("Enter a number to print its multiple table: "))
#for i in range(1,11):
 #   print(n, "X", i, "=", n*i)

# ***********************PASS Statement**********************
for i in range(10):
    pass 

# ***********************Practice 3**********************
# Print the sum of first P natural number
P = 9
sum = 0
for i in range(1, P+1):
    sum += i
print("The sum of first ", P, " natural numbers is: ", sum)
# Find the fectorial of a number P
P = 6
fac = 1
for i in range (1,P+1):
    fac *= i
print("The factorial of ", P, " is: ", fac)