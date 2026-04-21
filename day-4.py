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


