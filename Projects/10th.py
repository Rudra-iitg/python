# ***************************Practice1***************************
# Write a given programme in python
file = open("practice.txt","w")
file.write("Hi Everyone\nwe are lerning file I/O \nusing Python \nI like Programming in Python")
file.close()

# ***************************Practice2***************************
# Write a programme that will replace the word "Python" with "Java" in the file practice.txt
file = open("practice.txt","r")
data = file.read()
file.close()
data = data.replace("Python","Java")
print(data)
file = open("practice.txt","w")
file.write(data)
file.close()
