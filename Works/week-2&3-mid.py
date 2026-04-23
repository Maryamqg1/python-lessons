

#ph1-day-12-15-16-wknd2-13-14.py
#functions
def my_function():
  print("Maryam says Hello")  
  
my_function()

def go():
    print('start running')
go()
go()
go()

def get_water():
  return "Here is your water"

print(get_water())

def get_chocolate():
  return "Here is your chocolate"

action = get_chocolate()
print(action)

def Action(name1):
  print(name1 + " Hello")

Action("Tobi")
Action("Praise")
Action("John")

def greet(name1, name2):
  print(name1 + name2 + " Hello")
  print(f"{name1} {name2} Hello")

greet("Tobi", " Adebayo")
greet("Praise", " Adewumi")
greet("John", " Adetunji")
print ('how are you all doing today')

def Hobby(Hobby = "Skating"):
  print("I like ", Hobby)

Hobby("Swimming")
Hobby("Tennis")
Hobby()
Hobby("Gamming")

#day17
def Object(name,use):
    print("i have an object")
    print(f"the object is a {name}")
    print(f"i use the {name} to {use}")
Object('Gun', 'Shoot')
Object(name='pencil',use='draw')
Object('laptop', use = 'code')

def Statement(fruit):
  for f in fruit:
    print(f)

fr = ["apple", "banana", "cherry"]
Statement(fr)

def edible():
  return ["apple", "banana", "cherry"]

fruits = edible()
print(fruits[0])
print(fruits[1])

def foods(*food):
  print("The Best food is " + food[0])

foods("Rice", "Bread", "spag")

def my_command(greeting, *names):
  for name in names:
    print(greeting, name)

my_command("Hello", "Tobi", "Tife", "Peace")

def my_Statement(**Statement):
  print("Type:", type(Statement))
  print("Name:", Statement["name"])
  print("Age:", Statement["age"])
  print("All data:", Statement)

my_Statement(name = "Paul", age = 25, city = "Lagos")

def Letters(a, b, c):
  return a + b + c

numbers = [1, 1, 5]
result = Letters(*numbers)
print(result)