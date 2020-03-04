'''
Python es un lenguaje de programacion orientado a objetos
tiene propiedades y metodos 
'''
#ejemplos

class MyClass: 
  x = 5

print('-------------Crear objeto desde la clase o istanciar un objeto--------------------')

my_object = MyClass()
print(my_object.x)


print('-------------Funcion __init__()--------------------')

class Person:

  def __init__(self, name, last_name):
    self.name = name
    self.last_name = last_name

p1 = Person("Diego", "Tinitana")
print("los nombre es: {} {}".format(p1.name, p1.last_name))

p2 = Person("Andres", "Ortega")
print("los nombre es: {} {}".format(p2.name, p2.last_name))

print('-------------clases con funciones--------------------')
class Car:
  
  def __init__(self, model, year):
    self.model = model
    self.year = year
  
  def show_model(self): #funcion que ejecuta algo
    print('The model is:', self.model)
  
  def get_year(self): #funcion q retorna valor
    return self.year

c1 = Car("nissan", 2018)
print(c1.show_model())
year = c1.get_year()
print('year: ', year)

print('-------------clases con funciones privadas--------------------')
class User:
  
  def __init__(self, name, password):
    self.name = name
    self.__password = self.__encrypt_password(password) # con los '__' se declara varibles privadas

  def __encrypt_password(self, password): # funciones privadas se crean con '__'
    return password.upper()
  
  # def get_password(self):
  #   return self.__password

  @property
  def password(self):
    return self.__password
  
  @password.setter
  def password(self, valor):
    self.__password = self.__encrypt_password(valor)


u1 = User("diego", 'diego12')
print(u1.name)
print(u1.password)
u1.password = 'new password'
print(u1.password)

print('-------------clases con Variables de clases--------------------')
class Circle:
  
  _pi = 3.1416 # _ se antepone como convencion para saber q son variables de clase 
  _has_radio = True

  @staticmethod #metodo estatico q le pertenece solo a la clase
  def pi():
    return 3.1416
  
  @classmethod #metodo de clase q le pertenece solo a la clase
  def new(cls, radio):
    cls._has_radio = False
    return Circle(radio)
  
  # metodo de clase pueden alcanzar los atributos de la clase lo metodos estaticos no

  def __init__(self, radio):
    self.radio = radio 
  
  def area(self): #metodos de instancia
    return self.radio * self.radio * Circle._pi # se puede acceder a la variable de clase con nombre de la clase mas el atributo 'Circle.pi'

c1 = Circle(4)
c2 = Circle(3)

print(Circle._pi) # no es necesario instanciar la clase para tener las variables de clase
print(c1.__dict__) # se puede imprimir todas de la instancia
print(c1.area())
print(c1.radio)
print(c2.radio)
c3 = Circle.new(20)
print(">>>",c3._has_radio)

'''
Mas informacion:
https://www.w3schools.com/python/python_classes.asp
https://docs.python.org/3/
'''