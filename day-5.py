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