'''def Ind_fav(fruit):
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
print(yours())'''

'''def casing(words):
    def Action():
        return words().lower()
    return Action

@casing
def first ():
    return'MAVELOUS'
print (first())'''
    

'''def casing(words):
  def inn(x):
    return words(x).upper()
  return inn

@casing
def myfunction(name):
  return f"Hello {name}"

print(myfunction("John"))'''

'''def a1(n):
    return lambda a, c : a + c + n
def a2(u):
    return lambda b : b * u
a3 = a1(3)  
a4 = a2(5)
print(a3(11, 4))
print(a4(7))'''

class MyNumbers:
  def __iter__(self):
   
    self.a = 0
    return self

  def __next__(self):
    if self.a<=29:
        self.a += 3
        x = self.a

        return x
    else:
        raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#add
#commit
#push
