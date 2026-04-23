

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