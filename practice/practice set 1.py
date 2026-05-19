# 1. Create two variables,  a = 9  and  b = 40 , then write an expression to add them

a=100
b=789

c=a+b

print(c)



#2. What is the output of  type(123)  and  type("123") ?

print(type(123))      #<class 'int'>

print(type("123"))    #<class 'str'>



# 3. If  ab = "2345"  and  cd = "3253" , what happens when you write  ab + cd ?

ab="2345"
cd="3253"

print(ab+cd)    #23453253



# 4. How do you convert  ab  and  cd  to integers before adding them?

add= int(ab) + int(cd)
print(add)    #5598



# 5. If  name = "sahil" , what does  name.lower()  return?

name="sahil"
print(name.lower())    #sahil



# 6. What does  name.count("a")  return for  name = "sahil" ?

print(name.count("a"))      #1



# 7. What is the result of  len("Python") ?
print(len("Python"))    #6



# 8. What does  "Notebook"[0:3]  return?
print("Notebook"[0:3])    #Not



# 9. What does  "Python"[1:-1]  return?

print("python"[1:-1])    #ytho



# 10. Evaluate  11 // 2  and  11 % 2 .

print(11//2)     #5

print(11%2)      #1



# 11. What is the value of  2 ** 3 ** 2 ?

print(2 ** 3 ** 2)     #512



# 12. What is the result of  10 + 2 * 3 , and why?

print(10+2*3)        #16

# it happens through operator precedence
# the multiplication is performed first by higher precedence, and then the addition is performed



# 13. If  a = 45  and  b = 4 , what are the results of  a > b  and  a == b ?

a=45
b=4

a>b     #true
a==b    #false



# 14. If  b1 = True  and  b2 = False , what do  not(b1) ,  b1 and b2 , and  b1 or b2  return?

b1=True
b2=False

print(not(b1))     #False
print(b1 and b2)   #False
print(b1 or b2)    #True



# 15. What does  input()  return by default in Python?

# input() returns a string by default


# 16. Write a small program that takes two integer inputs and prints their sum.

num1=int(input("Enter first number: "))   #25
num2=int(input("Enter second number: "))  #35
print("Sum:", num1 + num2)                #Sum: 60



# 17. Write an  if-elif-else  block that prints whether a number is positive, negative, or zero.

num = int(input("Enter a number: "))  # Example: 5

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")



# 18. What is the difference between  if-elif-else  and  match-case ?

# if-elif-else:
# Used for checking conditions and logical expressions.

# match-case:
# Used for pattern matching and comparing specific values.



# 19. Write a  match-case  function that returns the message for HTTP status code  404 .

def http_status_message(status_code):
    match status_code:
        case 404:
            return "Not Found"
        case _:
            return "Unknown Status Code"
        
print(http_status_message(404))              #Not Found



# 20. Use an f-string to print  Python  left-aligned, right-aligned, and center-aligned in a field of width 10.

text = "Python"
print(f"{text:<10}")   #Left-aligned
print(f"{text:>10}")   #Right-aligned
print(f"{text:^10}")   #Center-aligned

# Python    
#     Python
#   Python  