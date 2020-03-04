'''
Herencias, herencias multiples, override
'''

class Animal():
  def terrestrial(self):
    return True

class Pet():
  name = '' # all pet need a name

  def show_name(self):
    print(self.name)

class Feline(Animal):
  def claws(self):
   return True

  def hunt(self):
    print('The feline is hunting')

class Cat(Feline, Pet):

  def show_name(self):
    Pet.show_name(self)
    print('My cat is called {}'.format(self.name))
  pass

class Jaguar(Feline):
  pass

cat = Cat()
print('cat: ', cat.claws())
print('cat: ', cat.terrestrial())
cat.name = 'Bender'
cat.show_name()

jaguar = Jaguar()
print('jaguar: ', jaguar.claws())
print('jaguar: ', jaguar.terrestrial())