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

    
    