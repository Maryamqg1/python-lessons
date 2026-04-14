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





