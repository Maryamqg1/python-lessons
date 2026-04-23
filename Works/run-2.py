#PIP

'''from camelcase import CamelCase
c = CamelCase()
txt = "hello world"
print(c.hump(txt))'''

'''try:
  print(x)
except:
  print("An exception occurred")
  
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
  
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
  
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
  
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
  
a = -1

if a < 0:
  raise Exception("Sorry, no numbers below zero")

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")'''

h = ["Visitors", "wonderland"]
print(f"Hello, {h[0]}. Welcome to {h[1]}!")

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt)

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

price = 59000
txt = f"The price is {price:,} dollars"
print(txt)

# python formar() method

#none statement
result = None
if result is None:
  print("No result yet")
else:
  print("Result is ready")
  
#is not
result = None
if result is not None:
  print("Result is ready")
else:
  print("No result yet")

#without return statement
def myfunc():
  x = 5

x = myfunc()
print(x)

#user input
name = input("What is your name?: ")
print(f"Hello, {name}!")

print("What is your gender?: ")
gender = input()
print(f"Hello {name}, you can use the {gender} restroom!")

age = input("What is your age?: ")
fav1 = input("What is your favorite color?: ")
fav3 = input("What is your favorite gift?: ")
date = input("What is your date of birth?: ")
print(f"let's get a {fav3} in a {fav1} colour for {name}, she is turning {age} on the {date} ")

import math
x = input("Enter a number:")

#find the square root of the number:
y = math.sqrt(float(x))

print(f"The square root of {x} is {y}")

y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x);
    y = False
  except:
    print("Wrong input, please try again.")

print("Thank you!")
