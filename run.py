##file-general
#datatypes
#strings,integers,floats,lists,dictionaries,tuple

#strings 
'maryam'
#dictionaries
{'key': 'value'}
{'tea ': 2}
#integers
34
#floats
3.66
#lists
['e']
#tuple
('ou')



x = float(4)
print(x)
y = int(x)
print(type(x))
print(type(y))
print(y)


a = """really long senntence \n written by me, on day \n one"""
print(a)

## strings as arrays
x = 'marya'
print(x[1])
print(x[-1]) #negative indexing

#slicing
x = 'i am a student'
y = x[2::2]
print(y)

#Boolean
m = 67
n = 8900
if m < n:
    print(f"{m} is greater than {n}")
else: 
    print('m is not greater than n')
    
    
# classwork
'''slice and check for membership'''
t = 'come home'
j = t[0:4]
print (j)
print (j in t)

print('#'*60)

#LIST
#what are the characteristics of a list
animal = ['hen', 'turkey', 'rabbit']
#methods of a list- a method is a function that belongs to an object of a class/class
"""to see the methods of a list
command: dir(<name-of-list>)
"""
print(dir(list))
#append - to add to a list
#clear - returns an empty list. 
print(animal)
animal.append('frog') 
print (animal) 
animal.clear()  
print (animal)
exist = animal.append('frog')
print (exist)
print(animal.__class__())
print(animal.remove('frog'))
l = 'goat'
print(animal.__add__([l]))
print(animal.__reduce__)
print(animal.clear())


'''animal.append('frog') /n print (animal) - adds frog into the list of animals'''  
'''animal.clear() /n print (animal) - clears everything in the list'''

#DICTIONARIES
{'key': 'values'}
#ordered
{1:'strings', 2:'lists', 'three': 3}

#sets
tool = {'pin', 'hammer', 'nail'}
for x in tool:
    print (x)
tool.add('tape')
print (tool)
tool.add('workspace')
print(tool)
nature = ['rain','tree','forest']
tool.update(nature)
print (tool)
nature.remove('rain')
print(nature)
print('='*20)
tool.remove('pin')
print(tool)
tool.discard('rain')
print(tool)
tool.pop()


#frozenset
o = frozenset({"apple", "banana", "cherry"})
x = set(({"apple", "banana", "cherry"}))
print(o)
print(x)
print(type(o))
print(type(x))
food = {'rice','beans','spag'}
print (x.union(food))
print(food|x|tool)

#if-el-else
weather = 30
if weather <= 5:
    print ('it is very very very cold')
elif weather > 5 and weather < 10:
    print ('it is manageably cold')
elif weather > 10 and weather < 17:
    print ('it is cool')
else:
    print (f'the weather is warm @ {weather} degrees')
    
    
print('FUNCTION SCOPE' + '@@'*10)

def myScope():
    '''
    local scope
    '''
    x = 10
    print(x)
    def innerScope():
        nonlocal x
        x = 40
        print(x)
        
    innerScope()
    return(x)
        
myScope()    



#Day1
y = 'hello '
print (y)
m = 'maryam'
print (m)
print (y + m)
print ('hello maryam')
print ('hello', 'maryam')
print("Hello"); print("How are you?"); print("Bye bye!")
print ('''hello \n goodbye''')

h = int(24)
t = int(h / 2)
s = float(t)
print (h, t, s)
print (type(s))
w = int(t + s)
g = w / 5
p = int(g)
r = float(p)
print (w,g,p,r)

print ('maryam')
print ('"Hello world"')

j = 'john'
e = 50
a = int(e/2)
print(j)
print ('my name is' , j, 'and i am', a, 'years old' ) 
print("wow!", 25, "years old?")
print('yes sir.')

A = T = X = 59
print (A,T,X)
H,G,J = "computer", "rice", "water"
D,B,W = ['hen', 'duck','camel']
object = 'umbrella'
Y=S=V= object
print(G,S)
print (w,W)
Tools = ['hammer', 'nail', 'saw']
T = Tools
T1,T2, T3 = 'hammer', 'nail', 'saw'
print ( T,T1,T2,T3 )

#function
p = "awesome"
def myfunc():
  print("Python is " + p)
myfunc()

e = "good"
def myfunc():
  e = "fantastic"
  print("Python is " + e)
myfunc()
print("Python is " + e)

E = "superb"
def myfunc():
 print("Python is " + E)
myfunc()

def myfunc():
  global M
  M = "Wonderful"
myfunc()
print("Python is " + M)

#day2
x = 5
y = 3.14
z = 'Hello'
'''print((type(x),(y),(z)))- this cannot execute 
all variable types involved in the statement'''
print (type(x))
print (type(y))
print (type(z))


t = 'come home'
j = t[0:4]
print (j)
print (j in t)
p = t[:] #invovles everything
u = t[5:]
s = t[0::3] #jumps but invovles the end character
print (s)
print(p)
print(u)
w = 'why'
print(w in t)

r = 45
o = 4500
if r < o:
    print ('r is less than o')
else:
    print ('r is not less than o')
g = (r > o)
print (g)
print (not g)

#strings
for b in "banana":
  print(b)


a = " Hello, Maryam! "
print(len(a))
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H", "Y"))
print(a.split(","))

#day3
x = 200
print(isinstance(x, int))
print(isinstance(x, str))

def myF() :
  return True

if myF():
  print("YES!")
else:
  print("NO!")
  
m = 360
m2 = 60
print (m + m2) # adds
print (m - m2) # subtracts
print (m * m2) # multiplies
print (m / m2) # returns the answer in float (with decimal)
print (m % m2) # modulous - divides and Gives the remainder
print (m ** m2) # exponention - raise to the power of - i.e multiply m by m , m2 times
print (m // m2) # floor division - returns answer in integer(whole number)
print (m | m2) # Converts to to binary , then uses the OR operation, then converts the result back to base 10
print(m == m2) # equal to
print(m != m2) # not equal to
print(m > m2) # greater than
print(m < m2) # less than
print(m >= m2) # greater than or equal to
print(m <= m2) # less than or eual to
print(m2 < m < 100)
print(m2 < m < 1000)

#logical operators
print(m2 < m and m < 100) # and - 	Returns True if both statements are true
print(m2 < m and m < 1000) 
print(m2 < m or m < 100) # or - Returns True if one of the statements is true
print(m2 < m or m < 1000)
print (not(m2 < m and m < 1000)) # not - Reverse the result, returns False if the result was true
print (not(m2 < m or m < 1000))
print (not(m2 < m and m < 100))
print (not(m2 < m or m < 100))
print ('*'*100)

#identity operators
# 'is' and 'is not' operations
''' is - Returns True if both variables are the same object - x is y, 
it is true when y is stated as y = x'''
''' is not - Returns True if both variables are not the same object - x is not y, 
it true when the y variable was given it's own individual assignment'''
# 'is' and '==' carry out different operations
m1 = m
m3 = ['rain','thunder','turnado']
M3 = ['rain','thunder','turnado']
print(m1 is m)
''''''
print(m3 is M3) 
print(m3 == M3)
''''''
print(m1 == m2)

print ('#'*100)
#memebership operators
# 'in' and ' not in' operations
''' in - for something in something - Returns True if a sequence with 
the specified value is present in the object '''
''' not in - for something in something - Returns True if a sequence with 
the specified value is not present in the object '''
m4 = ['melon','orange', 'guava']
m5 = ['juice','drink','smoothie']
M4 = m4 
print ('guava'in m4)
print ('guava'in M4)
print ('guava'in m5)
print ('orange' not in M4)

#day4
#The Bitwise funtion i.e logic gate 
#coverts to binary to carry out the operation 
#then back to base 10 when the result has been gotten.
''' '&' - AND - x & y - Sets each bit to 1 if 'both' bits are 1, 
if not the bit results to zero.
'|' - OR - Sets each bit to 1 if one or both bits is 1 - x | y
'^' - XOR - Sets each bit to 1 if only one of two bits is 1 - x ^ y
'~' - NOT - Inverts all the bits - ~x or result ~()
'<<' - Zero fill left shift - shift left while adding 0 from the right, 
the given amount of times, 
while dropping one bit at the left as 0 is added at the right -	x << 2
'>>' - Signed right shift - shift right while adding 0 from the left, 
the given amount of times, 
while dropping one bit at the right as 0 is added at the left '''

x = 360
y = 60
z = 3
print (x & y)
print ( x | y)
print (x ^ y)
print (~ x)
print (~ y)
print (~(x & y))
print (~( x | y))
print (~(x ^ y))
print (x << z)
print (x >> z)
print (y << z)
print (y >> z)

#changing list item
tools = ['hammer', 'nail', 'tape'] 
weather = ['rain','turnado','snow']
aninmals = ('fox','monkey','cat')
tools[2] = 'driller'
print(tools)
tools[0:] = ['shovel','hoe','cutlass']
print(tools)
tools.insert(1, 'axe') # to insert as index 1
print(tools)
tools.append('saw') # to add at the end
print(tools)
tools.extend(weather) # append with another list
print(tools)
tools.append(aninmals) # append with tuple
print(tools)
tools.remove(aninmals) # to remove the specified
print(tools)
tools.pop(7)
print(tools)
del tools [-1]
print (tools)
tools.sort()
print (tools)
tools.reverse()
print (tools)
tools.clear()
print(tools)
del tools

nature = weather.copy()
life = nature[:]
print(nature)
print(life)
life

#day5
#if-elif-else
#base value: is value we check our conditions against

age = 100

if age <=3:
    print('the person in question is a baby')
elif age >3 and age <=7:
 print ('the person in question is a toddler')
elif age >7 and age <=12:
    print ('the person in question is a child')
elif age >12 and age <=19:
    print ( 'the person in question is a teenager')
elif age >19 and age <=25:
    print ('the person in question is a youth')
elif age >25 and age <=30:
    print ('the person in question is a young adult')
elif age >30 and age <=35:
    print('the person in question is an adult')
else:
    print('the person in question is either getting old, already old, or very old')
    
years_spent = 1000
print ('you have many years ahead of you') if years_spent <= 30 else print ('you are nearing your end') if years_spent >30 and years_spent <=100 else print('you are a dead man')


weekday = 4

if weekday < 5:
    print('a working day')
    if weekday < 6:
        print('also a weekday')
else:
    print('6/7th day are weekends')
    
    
score = 90
if score >= 75:
    print ('Exellent')
    if score >= 85:
        print('Welldone! you made it to the top ranks')
else:
    print('you did well, but you can do better')
    
    


weekday = 'friday'
time = '3:00'
has_prayer_mat = True

if weekday == 'friday':
    if time == '1:00':
        print('time for prayer in the big_mosque')
    else:
        print('you may be too early or too late')
        if has_prayer_mat:
            print('you are ready for prayers')
        else:
            print('you are on time but not ready')
else:
    print('no jummah today')
    
print('##'*30)
    
# Indomie Ingredients
pot = fire = True
water = salt = True  #in specified quantity
indomie1 = 'Added'#in specified quantity
seasoning = 'Added' #in specified quantity
egg1 = ['Boiled','fried'] #in specified quantity


if pot and fire:
    if water and salt:
        if indomie1:
            if egg1:
                for egg_preference in egg1:
                    if egg_preference == 'Boiled':
                        print('nice choice go on cooking')
                    else:
                        print(f'{egg1[1]} is not the best choice for your noodles')
                        
                print('youve choosen your preference for eggs, lets get on with the cooking')
                if seasoning == 'Added':
                    print ('You are all set, let it cook for 7 minutes')
                    print(
                        '''cooking is a delight, waiting for 7miutes may be to long, but \nI think you can survive''')
                else:
                    print('indomie without seasoning is medicine')
            else:
                print('You need to boil the eggs first')
                
        else:
            print('Indomie is the only noodles you can make with my pot')
    else:
        print('fire without water makes no meal - get some salt and water please')
     
else:
    print('go to market')
                

print('@'*30)
    
#time__minutes
indomie2 = 3
egg2 = 17

if indomie2 == 7:
    print ('the indomie is perfectly cooked')
elif indomie2 < 7:
    print ('the indomie is not cooked')
elif indomie2 > 7:
    print ('the indomie is cooked but soogie')
if egg2 == 10:
    print ('the egg is perfectly boiled')
elif egg2 < 10:
    print('the egg is not cooked')
elif egg2 > 10:
    print ('the egg is overboiling')
else: 
    print('No comment')

#wknd1-6-7
#Quick Food - Chicken Soup
''' ingredients being - fire, pot, chicken, onions, ginger, garlic, seasonings - salt, 
maggie, curry, thyme, corriander, yaji,. 
spices, vegitables, water,''' # in specified quantities

Begin = 'start'
Protein = 'Chicken'
Aromatics = ['onions','ginger','garlic']
Seasonings = ['salt','maggie','curry','thyme','corriander','yaji']
spices = True # Optional
vegitables = ['saint leave', 'persley'] # Optional 
Mix = 'Mix in'
liquid = 'water'
base = ['pot', 'fire']
End = 'Done'

if Begin:
    print ("You need to wash your hands first then wash the chicken to get started.")
    if Protein:
        print ("Awesome, Now let's mix in our chopped onions, ginger, and garlic.")
        if Aromatics:
            print ("Great, Now Let's get Sesoning!")
            if Seasonings:
                print ("Perfect, Now is your chance to add in your spices, but be wise with your choices.")
                if spices:
                    print ("Wonderful, Now stir and Mix all the ingredients with the chicken, with both hands thoroughly.")
                    if Mix:
                        print ("Excellent, Now transfer it into ypur pot and add in your water.")
                        if liquid:
                            print ("Bravo, cover and place on midium heat for 45minutes but keep checking and stirring every 10minutes.")
                            if base:
                                print ("Not the best choice, but you can add in a vegitable of your choice after 35minutes.")
                                if vegitables:
                                    print ("Good, Now wait for another 10 minutes.")
                                    if End:
                                        print ("Fantastic, Now put off the fire, Serve and Enjoy!")
                                    else:
                                        print ("It still needs more time cooking.")
                                else:        
                                    print ("Nice, I respect your choice.")
                            else:
                                print ("You need a pot and fire to cook, unless you want to eat it as it is.")
                        else:
                            print ("Without water, it could get burnt and we don't want that. And we need water to make a soup!")
                    else:
                        print ("It needs to be mixed properly, to have a balanced taste.")
                else:
                    print ("The spices are not a must add but they give additional flavour.")
            else:
                print ("The seasonings are essential for it to be tasty.")
        else:
            print ("The Soup needs it's own base to have flavour.")
    else:
        print ("You can't cook chicken soup without the chicken.")
else:
    print ("Hygiene first, before anything.")

#day8
#match
Colour  = 'level 10'
match Colour:
    case 'level 1' :
        print ('white')
        
    case 'level 2':
        print ('yellow')
            
    case 'level 3':
        print ('orange')
        
    case 'level 4':
        print ('green')
        
    case 'level 5':
        print ('blue')
        
    case 'level 6':
        print ('pink')
        
    case 'level 7':
        print ('red')
        
    case 'level 8':
        print ('puple')
        
    case 'level 9':
        print ('black')
    case _ :
        print ('Colours add beauty and makes things lively')   
        
        
month = 5
day = 7
match day:
    case 1 | 2 | 3 | 4 | 5 | 6 | 7 if month == 1:
        print("A day in january")
    case 1 | 2 | 3 | 4 | 5 | 6 | 7 if month == 2:
        print("A day in february")
    case 1 | 2 | 3 | 4 | 5 | 6 | 7 if month == 3:
        print("A day in march")
    case 1 | 2 | 3 | 4 | 5 | 6 | 7 if month == 4:
        print("A day in April")
    case 1 | 2 | 3 | 4 | 5 | 6 | 7 if month == 5:
        print("A day in May")
    case _:
        print("No match")
        
        
#matching list
Month = [1,2,3,4,5]
Day = 7
match day:
    case 1 | 2 | 3 | 4 | 5 | 6 | 7 if Month[0] == 1:
        print("A day in january")
    case 1 | 2 | 3 | 4 | 5 | 6 | 7 if Month[1] == 2:
        print("A day in february")
    case 1 | 2 | 3 | 4 | 5 | 6 | 7 if Month[2] == 3:
        print("A day in march")
    case 1 | 2 | 3 | 4 | 5 | 6 | 7 if Month[3] == 4:
        print("A day in April")
    case 1 | 2 | 3 | 4 | 5 | 6 | 7 if Month[4] == 5:
        print("A day in May")
    case _:
        print("No match")
        
#while loop

i = 1
while i < 6:
    i += 1
    print(i)
  

z = 2
while z <= 20:
    
    z += 1
    if z == 15:
        break
    print(z)
    
print('#'*80) 

y = 3
while y <= 30 :
    
    y += 3
    if y == 21:
        continue
    print(y)
#day9
#For loops

i = 1 

while i <= 5:
    print(i)
    i += 1 #ascending
    
print ('@'* 99)
    
v = 5

while v >= 1:
    print(v)
    v -= 1 #descending

print ('#'* 99)
    
p = 1
# print (p % 2)
 
while p <= 10:
    if p % 2 == 0:
        print(p)
    p += 1
    
print ('~'* 99)
    
s = 1
total = 0

while s <= 5:
    total += s
    s += 1    

print("Total:", total)

#day10
''' Primitive Loops '''
#while loops
'''simple while loop, use break statement, use continue statement, 
use else statement'''

# simple while loops
q = 1
while q < 11:
    print (q)
    q +=1
    
p = 1 
while p <= 11:
    print (p)
    p +=1
    
s = 11
while s > 1:
    print (s)
    s -= 1
    
t = 11
while t >= 1:
    print (t)
    t -= 1
    
#using break statements
u = 1
while u < 15:
    print (u)
    if u == 7:
        break
    u += 1
    
j = 15
while j > 1:
    print (j)
    if j == (9):
        break
    j -=1
    
#use continue statement
g = 2
while g <= 12:
    print (g)
    g +=2
    if g == 6: 
        continue
    #'''prints  2 and 6'''


gb = 2
while gb <= 12:
    gb +=2
    print (gb) 
    if gb == 6:
        continue
    #'''exclude 2 but prints 6'''
    
gc = 2
while gc <= 12:
    gc +=2
    if gc == 6:
        continue
    print (gc) 
    #'''exclude both 2 and 6'''



h = 17
while h >= 1:
    print (h)
    h -=1
    if h == 7:
        continue

# use else statement
k = 0
while k <= 7:
    print (k)
    k += 3.5
    
else:
    print ('k is now equal to 7')
    
y = 7
while y >= 7:
    print (y)
    y -= 3.5
    print (y)
else:
    print ('y is now equal to 0')

#for loops
'''simple for loop, string loop, use break statement, 
use continue statement, use rage function, 
use else statement, use Nested loops, use pass statement '''

#simple for loops
protein = ['fish','chicken','meat','turkey','egg']
for y in protein:
    print (y)
    
#string loop
p_protein = 'chicken'
for t in p_protein:
    print (t)

#use break statement
juice = ['exotic','pulpy','peach']
for s in juice:
    print (s)
    if s == 'pulpy':
        break
    #'''includes pulpy'''

juice = ['exotic','pulpy','peach']
for s in juice:
    if s == 'pulpy':
        break
    print (s)
    #'''excludes pulpy'''
    
for t in 'drink':
    print (t)
    if t == 'i':
        break
    #'''includes i'''
    
for u in 'drink':
    if u == 'i':
        break
    print (u)
    #'''excludes i'''
    
#use continue statement
animal = ['rat','cat','dog']
for h in animal:
    if h == 'cat':
        continue
    print (h)
    #'''exludes cat but continues'''
    
animal = ['rat','cat','dog']
for h in animal:
    print (h)
    if h == 'cat':
        continue
    #'''includes cat then continues'''
    
#range function
for o in range(12): # starts from 0 ends at 11
    print (o)
    
for i in range(1,12): # starts from 1 ends at 11
    print (i)
    
for x in range(2,13,2): # starts from 2 , with the interval of 2, ends at 12
    print (x)  
    
#use else statemet
weapon = ['gun', 'rifle', 'arrow', 'spear', 'sword']
for k in weapon:
    print(k)
else:
    print ('No more Weapons Available')
    
#use nested loops
condition = ['ripe','sweet', 'nice', 'sour','bitter','unripe']
fruit = ['orange','watermelon','pawpaw','apple', 'grape']
for a in condition:
    for b in fruit:
        print(a,b)
        
#use pass statement
tools = ['tape', 'hammer', 'srews']
for l in tools:
    pass


#while and for loops
office = ['table', 'chair', 'canteen']
found = False

while not found:
    for r in office:
        if 'k' in r:
            print(r)
            found = True
            break
        
car = ['camery','toyota','lexus']
seen = False
while not seen:
    for c in car:
        if 'lexus' in c:
            print(c)
            seen = True
            break
        
shape = ['circle', 'square', 'oval']
count = 0

while count < 2:
    for k in shape:
        print(k)
    count += 1
    
'''Write code that:

- Loops through the list
- Stops completely when "knife" is found
- Prints only items before it'''

    
cutlery = ['spoon', 'fork', 'knife']
found = False
count  = 0
while count <= 1:
    for f in cutlery:
        print(f)
    count += 1
    break

        
while not found:
    for z in cutlery:
        if 'knife' in z:
            print(z)
            found = True
            break
    
while not found:
    for w in cutlery:
        found = True
        if 'knife' in w:
            break
        print (w)

#day11
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


#testing
name = ""

while name != "stop":
    name = input("Enter your name (type 'stop' to end): ")
    print("Hello", name)
    


while True:
    user_input = input("Enter a number (or 'q' to quit): ")

    if user_input.lower() == 'q':
        break

    if user_input.isdigit():
        num = int(user_input)
        print("You entered the number:", num)
    else:
        print("Invalid input. Enter a number or 'q' to exit.")
        

secret = 5
guess = 0

while guess != secret:
    guess = int(input("Guess the number: "))
    
    if guess == secret:
        print("Correct!")
    else:
        print("Try again")
        
num = 2
t = 1

while t <= 10:
    print(num, "x", t, "=", num * t)
    t += 1
    
password = ""

while password != "admin123":
    password = input("Enter password: ")

print("Access granted")

word = "Python"
o = 0

while o < len(word):
    print(word[o])
    o += 1
#modulous…
#--module.py
'''def myName(name):
    
    #function is imported in the useModule.py file
    

    return f'Hello, i am {name}'
#--useModule.py
import module
import datetime

print(module.myName('maryam') + ' and the today is ' + str(datetime.date.today()))'''

##testings
name = ""

while name != "stop":
    name = input("Enter your name (type 'stop' to end): ")
    print("Hello", name)
    


while True:
    user_input = input("Enter a number (or 'q' to quit): ")

    if user_input.lower() == 'q':
        break

    if user_input.isdigit():
        num = int(user_input)
        print("You entered the number:", num)
    else:
        print("Invalid input. Enter a number or 'q' to exit.")
        

secret = 5
guess = 0

while guess != secret:
    guess = int(input("Guess the number: "))
    
    if guess == secret:
        print("Correct!")
    else:
        print("Try again")
        
num = 2
t = 1

while t <= 10:
    print(num, "x", t, "=", num * t)
    t += 1
    
password = ""

while password != "admin123":
    password = input("Enter password: ")

print("Access granted")

word = "Python"
o = 0

while o < len(word):
    print(word[o])
    o += 1

##practices

#'''def Ind_fav(fruit):
def Aswr():
    return f"I love eating {fruit()}"
    return Aswr

@Ind_fav()
def mine():
    return 'Banana'

@Ind_fav
def yours():
    return 'Apple'

print(mine())
print(yours())

'''def casing(words):
    def Action():
        return words().lower()
    return Action

@casing
def first ():
    return'MAVELOUS'
print (first())'''
    

'''def casing(words):
  def inn(x):
    return words(x).upper()
  return inn

@casing
def myfunction(name):
  return f"Hello {name}"

print(myfunction("John"))'''

'''def a1(n):
    return lambda a, c : a + c + n
def a2(u):
    return lambda b : b * u
a3 = a1(3)  
a4 = a2(5)
print(a3(11, 4))
print(a4(7))'''

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
print(next(myiter))

#add
#commit
#push

##run
def Ind_fav(fruit):
    def Aswr():
        pronoun = 'I' if fruit.__name__ == 'mine' else 'You'
        return f"{pronoun} love eating {fruit()}"
    return Aswr

@Ind_fav
def mine():
    return 'Banana'

@Ind_fav
def yours():
    return 'Apple'

print(mine())
print(yours())


'''def Ind_fav(fruit, fruits):
    def Aswr():
        return f"I love eating {fruit()}"
    return Aswr

@Ind_fav
def mine():
    return 'Banana'

@Ind_fav
def yours():
    return 'Apple'

print(mine())
print(yours())'''

'''print('-------RECURSION-----------')
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
print(next(myiter))'''

'''import datetime

x = datetime.datetime(2027, 2, 27)

print(x)'''

'''import json
x =  '{ "name":"prospa", "age":35, "city":"Abuja"}'
y = json.loads(x)
print(f"{y[f'name']} is {y[f'age']} years old and lives in {y[f'city']}")'''

'''o = {
  "name": "John",
  "age": 30,
  "city": "New York"}
p = json.dumps(o)
j=json.dumps(o, indent=4, sort_keys=True)
print(p)
print(j)'''

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
