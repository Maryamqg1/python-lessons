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