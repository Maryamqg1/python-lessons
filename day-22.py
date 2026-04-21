#Decorators
#with a single function definition
def Race(Country):
    return Country
    
@Race
def Asian ():
    return 'China'
print (Asian())

@Race
def African ():
    return 'Ghana'
print (African())

def Food(Protein):
    return Protein
    
@Food
def mine():
    print ('eggs')
mine()

@Food 
def yours():
    print ('chicken')
yours() 

#with a double function definition
def Ind_fav(fruit):
    def Aswr():
        return fruit()
    return Aswr

@Ind_fav
def mine ():
    return 'Banana'

@Ind_fav
def yours ():
    return 'Apple'

print (mine())
print (yours())

def casing(words):
    def Action():
        return words().lower()
    return Action

@casing
def first ():
    return'MAVELOUS'
print (first())

