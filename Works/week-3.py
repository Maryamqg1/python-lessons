#day18
def names(list):
    def myname():
        return list()
    return myname

@names
def yourname ():
    return 'john'
print (yourname())

@names
def hisname ():
    return'peter'
print (hisname())

@names
def hername ():
    return'precious'
print (hername())

def Nation(country):
    def race ():
        return country()
    return race

@Nation
def white ():
    return 'America'
print (white())

@Nation
def black ():
    return 'Nigeria'
print(black())

@Nation
def Asians ():
    return 'China'
print(Asians())

#day19
#Functions
def city(): #creating a function named city
    print("We're in the city of Abuja") #the output you want to get when you call you function
city() #calling a function

#return statement
def Tools():
    return "The Tools i need are nails and a drilling machine set"
print (Tools())
#or
Needed_Tools = Tools()
print (Needed_Tools)

#pass statement when an there's no action
def colour():
    pass

#parameters and arguments
def colour(Type):
    print ("I Picked Colour", Type)
colour('Orange')

def student_course (Name,Department,Faculty,University = 'UniLag'): #stated in the braket is called parameter, it could be 1 or more , separated by a comma. a default parameter can be made using the '=' sign, and a default parameter must come last
    print(f'My name is {Name}, I am Schooling in {University}, studying {Department} in the faculty of {Faculty}')
student_course('Samuel','Cyber Security','Computing','University of Jos') #statemens in the bracket after the print statement are called arguments
student_course('Anne','Law','Art')
student_course('Abiola','Biomedical Engineering','Engineering','Havard University')

#with a return statement
def Individual_Occupation (Name,Workplace,Job = 'HR Manager'):
    return (f"My name is {Name}, i am a {Job} at {Workplace}")
print (Individual_Occupation('Paul','NNPC','Manager'))
print (Individual_Occupation('Johnson','Amron Global Servies','Project Manager'))
print (Individual_Occupation('Tola','Wema Bank'))

#to perform calculations

def Axis(x,y,z):
    return x+y+z
Destination = Axis(3,5,7)
print (Destination)

def cm_to_mm (cm):
    return (f"{cm}cm is {cm * 10}mm in mm ")
print (cm_to_mm(26))
print (cm_to_mm(55))
print (cm_to_mm(345))

#Keyword Arguments
def Collection(object,book):
    print(f"I have {object} and {book} in my special collection")
Collection(object = 'a golden wristwatch', book = 'an award wining novel') #keyword argument

def Schedule(Morning,Afternoon,Night):
    print (f'i have a {Morning} to attend in the Morning, then a {Afternoon} in the Afternoon, and a {Night} at Night')
Schedule('Program', Afternoon = 'Meeting', Night = 'Dinner')

#using different data types
#list
def Genre(Types):
    for i in Types: #for loops
        print(i) 
Available = ['Comedy','Romance','Horror','Adventure','Si-fi','Action','Triller','Reality','History','Docummentry']
Genre(Available)

#dictionaries
def Genre(Individual):
    print(f"Name: {Individual['Name']}")
    print(f"Preference: {Individual['Preference']}")
Indv = {'Name': 'Micheal', 'Preference': 'Triller'}
Genre(Indv)

#with return statement
#list
def Genre():
    return ['Comedy','Triller','Horror']
Types= Genre()
print(Types[0])

#Tuple
def Age():
    return (55,29)
a,b = Age()
print('Paul:', a)
print('Peter:', b)

#multiple arguments and keyword arguments
#arbitrary arguments - *args for multiple arguments for 1 parameter
def Students(*Oldest):
    print(f"The Oldest Student in the class is {Oldest[2]}")
Students('obinna','Augusten','Mavelous','Ifunaya')

def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Tobi", "Bolu", "Emanuella")
    
def Action(Greet,*guests):
    for guest in guests:
        print (Greet, guest)
Action('Morning', 'Amaka', 'Alex', 'Praise', 'Ibrahim', 'Asmau')

def Titles(Title, *names):
    for T in names:
        print(Title, T)
Titles('Mr', 'Peter', 'Sam', 'Solomon')

#arbitrary keyword argument - **kwargs
def Employees(**Roles):
    print(f"The manager is {Roles['Manager']}")
Employees (CEO = 'Alex', Manager = 'Precious', Secetery = 'Tife')

def my_function(**kwargs):
  print("Type:", type(kwargs))
  print(f"Name: {kwargs["name"]}")
  print(f"Age: {kwargs["age"]}")
  print(f"All data: {kwargs}")
my_function(name = "Peter", age = 25, city = "Lagos")

def Staffs(Title,**Subject_Teacher):
    print(f"The Teacher taking Physics is {Title} {Subject_Teacher['Physics']}") 
Staffs('Mr/Mrs', English = 'Praise', Physics = 'Paul', Chemistery = 'Ahn')

def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print("  ", key + ":", value)

my_function("Max_3", age = 25, city = "Abuja", hobby = "Boxing")

#*args and **kwargs together
def Staffs(*Title,**Subject_Teacher):
    print(f"The Teacher taking chemistry is {'Mr' if Title[0] == 'Mr' else 'Mrs'} {Subject_Teacher['Chemistry']}") 
Staffs('Mrs','Mr', English = 'Praise', Physics = 'Paul', Chemistry = 'Annabel')
    
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Max", "Adetunji", age = 25, city = "Lagos")

#wknd3-20-21
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

#Decorators

