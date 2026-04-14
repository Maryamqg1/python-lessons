def names(list):
    def myname():
        return list()
    return myname

@names
def yourname ():
    return 'john'
print (yourname())

@names
def hisname ():
    return'peter'
print (hisname())

@names
def hername ():
    return'precious'
print (hername())

def Nation(country):
    def race ():
        return country()
    return race

@Nation
def white ():
    return 'America'
print (white())

@Nation
def black ():
    return 'Nigeria'
print(black())

@Nation
def Asians ():
    return 'China'
print(Asians())

