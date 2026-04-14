def Ind_fav(fruit):
    def Aswr():
        return f"I love eating {fruit()}"
    return Aswr

@Ind_fav()
def mine():
    return 'Banana'

@Ind_fav
def yours():
    return 'Apple'

print(mine())
print(yours())

'''def casing(words):
    def Action():
        return words().lower()
    return Action

@casing
def first ():
    return'MAVELOUS'
print (first())'''
    

def casing(words):
  def inn(x):
    return words(x).upper()
  return inn

@casing
def myfunction(name):
  return f"Hello {name}"

print(myfunction("John"))


