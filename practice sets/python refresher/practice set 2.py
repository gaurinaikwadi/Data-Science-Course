# A. Loops

# 1. What is the difference between a  for  loop and a  while  loop in Python?

# A for loop is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects. 
# It executes a block of code for each item in the sequence. A while loop, on the other hand, repeatedly executes a block of code as long as a specified condition is true. 
# The main difference is that a for loop is generally used when the number of iterations is known beforehand, while a while loop is used when the number of iterations is not known and depends on some condition being met.



# 2. Write a  for  loop to print all numbers from  1  to  10 .

for i in range(1, 11):
    print(i)       
                    #1
                    #2
                    #3
                    #4
                    #5
                    #6
                    #7
                    #8
                    #9
                    #10



# 3. Write a  while  loop that prints numbers from  5  to  1  in reverse order.
i=5
while i>=1:
    print(i)        #5
                    #4
                    #3
                    #2
                    #1
    i-=1



# 4. Write a loop that prints all even numbers from  1  to  20 .

for i in range(2, 21, 2):
    print(i)        #2
                    #4
                    #6
                    #8
                    #10
                    #12
                    #14
                    #16
                    #18
                    #20



# 5. Write a loop that skips the number  5  and stops when it reaches  10 .
for i in range(1, 11):
    if i == 5:
        continue
    print(i)        #1
                    #2
                    #3
                    #4
                    #6
                    #7
                    #8
                    #9
                    #10



# B. Lists

# 6. Create a list of five numbers and change the second element.

numbers = [1, 2, 3, 4, 5]
numbers[1] = 20 
print(numbers)     #[1, 20, 3, 4, 5]


# 7. Use  append()  to add a new item to a list.

fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)     #['apple', 'banana', 'cherry', 'orange']



# 8. Use  extend()  to merge two lists.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)     #[1, 2, 3, 4, 5, 6]



# 9. Write code to insert a value at index  2  in a list.
my_list = [1, 2, 4, 5]
my_list.insert(2, 3)
print(my_list)     #[1, 2, 3, 4, 5]



# 10. Sort a list in ascending order and print both the original and sorted versions
original_list = [5, 2, 9, 1, 5]
sorted_list = sorted(original_list)
print("Original list:", original_list)   #Original list: [5, 2, 9, 1, 5]
print("Sorted list:", sorted_list)       #Sorted list: [1, 2, 5, 5, 9]



# C. Tuples


# 11. What is a tuple, and how is it different from a list?

# A tuple is an ordered collection of items that is immutable, meaning that once a tuple is created, its contents cannot be changed. 
# In contrast, a list is a mutable collection of items that can be modified after creation (you can add, remove, or change items in a list).



# 12. Create a tuple with three items and print the second item.

my_tuple = (10, 20, 30)
print(my_tuple[1])     #20



# 13. Write code to unpack a tuple into three variables.

my_tuple = (10, 20, 30)
a, b, c = my_tuple
print(a)     #10
print(b)     #20
print(c)     #30



# 14. Create a single-element tuple and print its type.

single_element_tuple = (42,)
print(type(single_element_tuple))     #<class 'tuple'>



# 15. Write code to use  count()  and  index()  on a tuple.
my_tuple = (10, 20, 30, 20)
print(my_tuple.count(20))     #2
print(my_tuple.index(30))     #2



# D. Sets

# 16. Create a set from a list with duplicate values.

numbers = [1, 2, 3, 2, 4, 1, 5]

# Convert list to set
unique_numbers = set(numbers)

# Print the set
print(unique_numbers)

a=set(numbers)        #{1, 2, 3, 4, 5}


# numbers → original list with duplicates
# set(numbers) → removes duplicates
# unique_numbers → stores the final unique values


# 17. Add a new element to a set using  add() .

set1={1,2,3}

set1.add(7)

print(set1)        #{1, 2, 3, 7}


# 18. Use  update()  to add multiple items to a set.

set1.update([6,7,8])
print(set1)             #{1, 2, 3, 6, 7, 8}


# 19. Write code to find the union of two sets and print the result.

setx={7,8,9,6}
sety={1,2,3,4}

result=setx.union(sety)
print(result)              #{1, 2, 3, 4, 6, 7, 8, 9}



# 20. Write code to find the intersection of two sets and print the result.


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.intersection(set2)

print(result)            #{3, 4}


# E. Dictionaries

# 21. What is a dictionary in Python?
# A dictionary in Python stores data in key : value pairs.


# 22. Create a dictionary for a student with name, age, and grade.

student = {
    "name": "Gauri",
    "age": 20,
    "grade": "A+"
}

print(student)     #{'name': 'Gauri', 'age': 20, 'grade': 'A+'}



# 23. Access a value using a key and print it.

print(student["name"])     # Gauri
print(student["age"])      # 20
print(student["grade"])    # A+



# 24. Use  get()  to access a missing key with a default value.
print(student.get("city", "Not Found"))     #Not Found


# 25. Use  update()  to change one value and add one new key

student.update({
    "age": 19,
})

print(student)     #{'name': 'Gauri', 'age': 19, 'grade': 'A+'}


# F. File Handling and JSON

# 26. Write code to create a text file and write a line into it.

file = open("sample.txt", "w")

file.write("Hello, this is a text file.")

file.close()


# 27. Write code to read the contents of a text file using  with open() .
with open("sample.txt", "r") as file:
    content = file.read()

print(content)        #Hello, this is a text file.



# 28. Save a Python dictionary to a JSON file.

import json
from unicodedata import name

student = {
    "name": "Gauri",
    "age": 20
}

with open("student.json", "w") as file:
    json.dump(student, file)                #{'name': 'Gauri', 'age': 20}


# 29. Read a JSON file and convert it back into a Python object.

import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data)


# 30. Write code to append a new line to an existing file


with open("sample.txt", "a") as file:
    file.write("\nThis is a new line.")



# Challenge Tasks

# Write a small program that uses a list, a loop, and a condition together.
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        print(num, "is even")    #2 is even   
                                 #4 is even


# Create a dictionary of student details and print all key-value pairs.
student = {
    "name": "gauri",
    "age": 20,
    "course": "Data Science"
}

for key, value in student.items():
    print(key, ":", value)         #name : gauri
                                   #age : 20
                                   #course : Data Science



# Read and write a text file using  with open() .

with open("demo.txt", "w") as file:
    file.write("Hello Python")

# Read from file
with open("demo.txt", "r") as file:
    print(file.read())                  #Hello Python


    
# Convert a Python dictionary to JSON and back.
import json

data = {
    "name": "Gauri",
    "age": 20
}

# Convert to JSON
json_data = json.dumps(data)

print(json_data)                      #{"name": "Gauri", "age": 20}

# Convert back to dictionary
python_data = json.loads(json_data)

print(python_data)                    #{'name': 'Gauri', 'age': 20}




#Create a class with one attribute and one method.

# Create a class
class Student:

    # Attribute
    name = "Gauri"

    # Method
    def display(self):
        print("Student Name:", self.name)

# Create object
s = Student()

# Call method
s.display()

#Student Name: Gauri