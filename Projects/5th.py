# **********************Loops In Python**********************
# 1. For Loop
# 2. While Loop
# 3. Nested Loop
# 4. Loop Control Statements
# 5. Looping Techniques
# 6. Looping Functions
# 7. Looping Arrays and Lists
# 8. Looping Through a String
# 9. Looping Through a Tuple
# 10. Looping Through a Set
# 11. Looping Through a Dictionary
# 12. Looping Through a Range
# 13. Looping Through a Function        

# 1. For Loop
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
list = [23 , 45, 67, 89, 90, "Hello", "World", "Python"] # Same for tuple, set, dictionary, string
for val in list:
    print(val)
else:
    print("The loop is completed")
# 2. While Loop
# With the while loop we can execute a set of statements as long as a condition is true.
count = 1  # This variable ("count") is called as "Iteration Variable"
while count < 6:
    print("Hello, World!")
    count += 1

i = 5
while i <= 10:
    print(i, "Hello, World!")
    i += 1

# ***********************Practice 0**********************
# Search for a number X in the tuple using for loop
nums = (1,4,9,16,25,36,49,64,81,100,81)
X = 81
idx = 0
for el in nums:
    if(el==X):
        print("Number found at index: ", idx)
    idx += 1
# **********************Practice 1**********************
# Print a multiple table of a number n using while loops
print("Enter a number to print its multiple table: ")
n = int(input())
i = 0
while i <=10:
    print(n , " X ", i, " = ", n*i )
    i += 1

# **********************Practice 2**********************
# Print a number of square tables from 1 to 100 using while loops
i = 1
while i<= 100:
    print(i,"²", "=", i*i)
    i +=1

# **********************Practice 3**********************
 # the same above but using list method
nums = [1,4,9,16,25,36,49,64,81,100]
index = 0
while index < len(nums):
    print(nums[index])
    index += 1

# **********************Practice 4**********************
 # Search for a number X in the tuple using while loop
num = (1,4,9,16,25,36,49,64,81,100)
X = 64
i = 0
while i < len(num):
    if num[i] == X:
        print("Number found at index: ", i)
        break
    i += 1