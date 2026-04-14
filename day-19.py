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

