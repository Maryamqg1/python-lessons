#unpacking list
def my_routine (first, second, third):
    print(f"i would {first} then {second} and {third} ")
Today = ['Clean', 'Cook', 'Eat']
my_routine(*Today)

def Order (Oldest, Mid, Youngest):
    return f"Bola is {Oldest} years old presently, while Tola is {Mid} and being the youngest Firi is {Youngest}"
Age = [29, 25, 21]
Hierachy = Order(*Age)
print (Hierachy)

#Unpacking Dictionaries
def Instrument(Mshl, El, Lm):
  print (f"Misheal plays the {Mshl}, while Ella plays the {El} and the person that is incharge of the {Lm} is Liam")
Position = {'Mshl' : 'Guitar', 'El' : 'Piano', 'Lm' : 'Drums'}
Instrument(**Position)

def Program(Entrance, Guests, Stage, Refreshments, Exit):
  return f"the person incharge of manning the Entrance will be {Entrance} then for attending to the guest would be {Guests}, and {Stage} would be backstage, then {Refreshments} would be incharge of sharing Refreshments and {Exit} would be at the Exit"
Volunteers = {'Entrance' : 'Bola', 'Guests' : 'Rayhan', 'Stage' : 'Tola', 'Refreshments' : 'Bello', 'Exit' : 'Ben'}
Order = Program(**Volunteers)
print(Order)

#Scope
#Local Scope - Variable created inside of a function
def my_call():
    Takes = 5 #Local Scope
    print (f"{Takes} Takes shall be Taken")
my_call()


def Time (x): #as a parameter
    print(f"The time taken is {x}")
Time(7)

#A function another function - inner scope
def first_layer ():
    layer = 3
    def second_layer():
        print (layer)
        def third_layer():
            print(3*layer)
        third_layer()
    second_layer()
first_layer()
  
#Global Scope
TypeA = 65

def Type():
    TypeB = 34
    print (TypeB) # TypeA can also be called here
Type()

print (TypeA) #TypeB can't be called be called here

Type1 = 71

def Type():
  Type1 = 55
  print (Type1)
Type()

print(Type1)

# To creacte a global variable withtin a function
def Type():
  global Type3 
  Type3 = 75
Type()
print(Type3)  

#To change the value of a global variable
TypeC = 51
def Type():
  global TypeC 
  TypeC = 35
  print (TypeC) 
Type()
print(TypeC)

#nonlocal - to belong to a higher/outer function - reasignment
def first_input():
    m = 'maryam'
    def second_input():
        nonlocal m
        m = 'maya'
        print (m) #you can either put the print statement here
    second_input()
    print (m)     #or here
first_input()

#with return statement
def names ():
  Ben = 'Benjamin'
  def names2 ():
    nonlocal Ben
    Ben = 'Benedict'
  names2()
  return Ben
print (names()) #printing like this
n2 = names()    #or like this
print (n2)

#Python search order - LEGB RULE
'''Local - Inside the current function
Enclosing - Inside enclosing functions (from inner to outer)
Global - At the top level of the module
Built-in - In Python's built-in namespace'''

x = "global" # for 3

def outer():
  x = "enclosing" # for 2
  def inner():
    x = "local" # for 1
    print("Inner:", x) # for 1
  inner()
  print("Outer:", x) # for 2

outer()
print("Global:", x) # for 3