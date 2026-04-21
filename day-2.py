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
