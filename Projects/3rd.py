# **********************************List**********************************(Almost same as arrays)

marks = [97.34 , 98.56 , 99.23 , 100.00]
print(marks)
print(type(marks)) # <class 'list'>
print(marks[0]) # 97.34
print(marks[1]) # 98.56     
print(marks[2]) # 99.23
print(marks[3]) # 100.0

# ****************List slicing****************

print(marks[-1]) # 100.0
print(marks[-2]) # 99.23
print(marks[ :3])
# ****************We can store any type of data in a list whether it is float or int or string etc****************

string = ["Hello" , "World" , 2453 , 457.54 , "C++"]
print(string)

# ****************We can change the data of a list****************

string[0] = "Hi"
print(string)

# ***********************List Methods***********************
list = [6, 54, 34 , 35, 665, 54]

    # ****************append()****************

list.append(6)  #i.e. we just added 6 at the end of the list
print(list) # [6, 54, 34, 35, 665, 54, 6]

    # ****************List sort (ascending order)****************

list.sort() # [6, 6, 34, 35, 54, 54, 665] 
print(list) # [6, 54, 34, 35, 665, 54]

    # ****************List sort (descending order)****************

list.sort(reverse = True) # [665, 54, 54, 35, 34, 6, 6]
print(list) 

    # ****************reverse()****************

list.reverse() # [6, 6, 34, 35, 54, 54, 665]
print(list) 

    # ****************insert()****************

list.insert(2, 100) # [6, 6, 100, 34, 35, 54, 54, 665]
print(list) 

    # ****************pop()****************

list.pop() # [6, 6, 100, 34, 35, 54, 54] it will remove the last element
print(list) 

    # ****************remove()****************

list.remove(100) # [6, 6, 34, 35, 54, 54]
print(list)



# ***********************Tuple***********************

# ****************Tuple is immutable i.e. we can't change the data of a tuple****************

tup = (1, 2, 3, 4, 5, 1)
print(tup)
print(type(tup)) # <class 'tuple'>

tup1 = (1,)  # If we want to create a tuple with only one element then we have to put a comma after the element
print(tup1)

# ****************Tuple methods****************
    
    # ****************count()****************   

print(tup.count(1)) # 2 i.e. it will return the count of 1 in the tuple

    # ****************index()****************

print(tup.index(3)) # 2 i.e. it will return the index of 3 in the tuple

# ***********************Sets***********************

# ****************Sets are unordered and unindexed****************

number = {1, 2, 3, 4, 5, 1}
print(number)
print(type(number)) # <class 'set'>

items = {1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, "Hello", "Hello", "World"} # It will remove the duplicate elements
print(items)
 # ****************Create an empty set****************
collection = set()
print(type(collection)) # <class 'set'>

# ****************Set methods****************
collection.add(11)
collection.add(12)
collection.add(13)
collection.add(14)
collection.add(15)
collection.add("My name is Rudra")
print(collection) # {11, 12, 13, 14, 15, 'My name is Rudra'}
collection.remove(15)
print(collection) # {11, 12, 13, 14}
collection.discard(14)
print(collection) # {11, 12, 13}
print(len(collection)) # 3
collection.clear()
print(len(collection)) # 0
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(4)
collection.add(5)
collection.add("Hello")
collection.add("World")
print(collection) # {1, 2, 3, 4, 5, 'Hello', 'World'}
print(collection.pop()) # 1

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2)) # {4, 5}
print(set1.difference(set2)) # {1, 2, 3}
print(set1.symmetric_difference(set2)) # {1, 2, 3, 6, 7, 8}

    # ****************add()****************

# **************************Practice1**************************

movlist = []  

# Method 1
    # mov1 = input("Enter your favourite movie: ")
    # mov2 = input("Enter your 2nd favourite movie: ")
    # mov3 = input("Enter your 3rd favourite movie: ")
    # movlist = [mov1, mov2, mov3]
# Method 2
    # movlist.append(mov1)
    # movlist.append(mov2)
    # movlist.append(mov3)
# Method 3
    # movlist.append(input("Enter your favourite movie: "))
print(movlist)

# **************************Practice2**************************
 # To find palindrome in a list
 # We will use copy() method to copy the list
list_a = [1, 2, 3, 3, 2, 1]
list_b = list_a.copy()
list_b.reverse() 
if (list_a == list_b):
    print("Palindrome")
else:
    print("Not Palindrome")

# **************************Practice3**************************

# Get input from the user and store it in a dictionary and print it

result = {}
x = int(input("Enter marks in Physics: "))
result.update({"Physics": x})
y = int(input("Enter marks in Chemistry: "))
result.update({"Chemistry": y})
z = int(input("Enter marks in Maths: "))
result.update({"Maths": z})
print(result)

