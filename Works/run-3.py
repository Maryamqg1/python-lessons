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