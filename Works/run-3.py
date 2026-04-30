#Classes
class Individual:
  #class level properties
  name ="Man"
  age = 1000
#object of the person class
indv1 = Individual() #instance of a class
print(indv1.name)
print(indv1.age)

#changing the property value in class
Individual.name = 'Woman'
print(indv1.name)
Individual.name, Individual.age = 'Woman', 500
print(indv1.name, indv1.age)

Individual.country ='kenya'
print(indv1.country)


#Classes
class Food:
  #class level properties
  name ="rice"
  type = 'carbohydrate'
  
  #method/function of a class
  def myfood(self):
    print(f"my food is {self.name} and it is a {self.type}")
  
    
#object of the person class
food1 = Food() #instance of a class
print(food1.name)
print(food1.type)

food1.myfood()

#changing the property value in class
Food.name = 'chicken'
print(food1.name)
Food.name, Food.type = 'chicken', 'protein'
print(food1.name, food1.type)

#creating classes with an init function
class Transportation:
  def __init__(self,type,colour = 'white'):
    self.type = type
    self.colour = colour
Train = Transportation('train')
print(f'I borded a {Train.colour} {Train.type}')

print('=======METHODS OF A CLASS=========')

class Vehicle:
  #class level properties
  '''
  access : classname.propertyname
  usage: Vehicle.manual
  result: ''
  '''
  manual = ''
  
  #object level properties
  '''
  access: Objectname.propertyname
  usage: car1.brand, car1.model
  '''
  def __init__(self,brand, model):
    self.brand = brand
    self.model = model
   
   #methods/functions of a class 
  def myfunc(self):
    print(f"My vehicle is a {self.model} {self.brand}`")
    
  #method to change the value of a class level property
  def change_manual(self):
    Vehicle.manual = 'new manual'
    
    
car1 = Vehicle('Toyota', 'Corolla')
print(car1.brand)
print(car1.model)

car1.myfunc()
print(Vehicle.manual)
car1.change_manual()

print('===METHODS WITH PARAMETERS===')
class Sum:
  def num(self, a, b):
    return f'This is the sum of {a} and {b}: {a + b}'
  
sum1 = Sum()
print(sum1.num(5, 10))


print('==METHODS ACCESSING PROPERTIES==')
class Students:
  def __init__(self,  average, score=80):
    self.score = score
    self.average = average
    
  #function that mod a prperty of the class
  def check_score(self):
    if self.score > self.average:
      self.score += 1
      return 'Above average'
    else:
      self.score -= 1
      return 'Below average'
    
  #object
student1 = Students(average=75, score=10)
print(student1.check_score())
print(student1.check_score())

print('====INHERITANCE====')
class parent:#base class
  def __init__(self, name, habitat):
    self.name= name
    self.habitat= habitat
    
  def move(self):
    return f'{self.name} now lives in {self.habitat}'
  
class child(parent): #derived class
  #child class inherits the properties and methods of the parent class
  def __init__(self, name, habitat, age, gender):
    parent.__init__(self, name, habitat) #calling the init function of the parent class
    self.age = age
    self.gender = gender
    
  def move(self):
    return f'{self.name} is a {self.age} year old {self.gender} that now lives in {self.habitat}'
  
parent1 = parent(name='John', habitat='New York')
print(parent1.move())  
child1 = child(age=10, gender='male', name='Jack', habitat='Los Angeles')
print(child1.move())

class mylife:
  def __init__(self, name, age, hobby):
    self.name = name
    self.age = age
    self.hobby = hobby
    
  def status(self):
    return f'{self.name} is {self.age} years old and loves {self.hobby}'
  
  
class mystatus(mylife):
    def __init__(self, name, age, hobby, job):
      mylife.__init__(self, name, age, hobby)
      self.name = name
      self.age =age
      self.hobby = hobby
      self.job = job
      
    def status(self):
      return f'{self.name} is a {self.age} years old {self.job} that likes {self.hobby}'
  
mylife1 = mylife(name='Annabelle', age=25, hobby='dancing')
print(mylife1.status())
mystatus1 = mystatus(name='Annabelle', age=25, hobby='dancing', job='Accountant')
print(mystatus1.status())

