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

