
def Ind_fav(fruit):
    def Aswr():
        return f"I love eating {fruit()}"
    return Aswr

@Ind_fav
def first():
    return 'Banana'

@Ind_fav
def second():
    return 'Apple'

print(first())
print(second())

#adding specified pronouns

def spd_fav(favs):
    def Aswr():
        pronoun, fruits = favs()
        return f"{pronoun} love eating {fruits}"
    return Aswr

@spd_fav
def mine():
    return 'I','Banana'

@spd_fav
def yours():
    return 'You','Apple'

print(mine())
print(yours())

# different style
def Ind(pronoun):
    def Fav(fruit):
        def Aswr():
            return f"{pronoun} love eating {fruit()}"
        return Aswr
    return Fav


@Ind ("I")
def first():
    return "Banana"

@Ind ("You")
def second():
    return "Apple"

print(first())
print(second())

#changing casing
def casing(words):
    def Action():
        return words().lower()
    return Action

@casing
def first ():
    return'MAVELOUS'
print (first())
    
def casing(words):
  def inn(x):
    return words(x).upper()
  return inn

@casing
def myfunction(name):
  return f"Hello {name}"

print(myfunction("John"))

print('-------RECURSION-----------')

def func(n):
    #base case is a condition under which the recursion will stop
    if n <=10:
        print(n * 2)
    else:
        return func(n - 1)
    
func(12)
 
def func(n):
    base_case = 10
    if n <= base_case:
        print(n * 2)
    else:
        return func(n - 1)
    
func(9)   
    
def maya(n):
    #base case
    base_case = 0
    if base_case <= 5:
        print('I am the base case')
        base_case = base_case + 1
    else:
        return maya(n - 1) #recursion
  
       
maya(5)

def countdown(n):
  if n >= 5:
    print("Done!")
  else:
    print(n)
    countdown(n + 1)

countdown(0)

print('------GENERATOR WITH VARIABLE---------')
def my_gen():
    while True:
      recieved = yield
      print(f'RECEIVED: {recieved}')
      
var = my_gen()
next(var)

for i in [1,2,3,4,5]:
    var.send(i)
    
    
print('=====GENERATORS')
    
def my_gen():
    while True:
      recieved = yield
      print(f'RECEIVED: {recieved}')
      
var = my_gen()
next(var)

for i in [1,2]:
    var.send(i)

## ITERATORS
my_tuple = ('me', 'you')
y = iter(my_tuple)

print(next(y))
print(next(y))

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class MyNumbers:
  def __iter__(self):
    self.a = [0,7,14,21,28]
    return self

  def __next__(self):
    x = self.a
    A = [y for y in range(0,30,3)]
    self.a.append(A)
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

import datetime

x = datetime.datetime(2027, 2, 27)

print(x)

def a1(n):
    return lambda a, c : a + c + n
def a2(u):
    return lambda b : b * u
a3 = a1(3)  
a4 = a2(5)
print(a3(11, 4))
print(a4(7))

class MyNumbers:
  def __iter__(self):
   
    self.a = 0
    return self

  def __next__(self):
    if self.a<=29:
        self.a += 3
        x = self.a

        return x
    else:
        raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
'''print(next(myiter))''' # prints stopiteration error because the condition is not met


import json
x =  '{ "name":"prospa", "age":35, "city":"Abuja"}'
y = json.loads(x)
print(f"{y[f'name']} is {y[f'age']} years old and lives in {y[f'city']}")

o = {
  "name": "John",
  "age": 30,
  "city": "New York"}
p = json.dumps(o)
j=json.dumps(o, indent=4, sort_keys=True)
print(p)
print(j)

import json
import re
status = "The forest is filled with Animals"
state = re.search("Animals", status)
if state:
    print('The word is present')
else:
    print('The word is not present')

politics = 'Tinubu must go'
opinion = re.search("Tinubu", politics)
if opinion:
    print('Tinubu is still the president')
else:
    print('Tinubu has left')
    
Animals = "There are birds,fishes,snakes,monkeys,lions and elephants in the forest"
present = re.search("snakes|Lions", Animals)
if present:
    print('The forest is not safe')
else:
    print('The forest is safe a bit')
    
Type = re.findall("T..e",  Animals)
print(Type)
