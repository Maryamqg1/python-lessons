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


    
    
