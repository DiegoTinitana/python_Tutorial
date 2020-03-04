'''
Es una porción de codigo que solo se ejecuta
cuando es llamada.
las funciones en python se declaran con la
palabra reservada "def" y el nombre de la funcion
'''
#ejemplos

def my_fuction():
  pass              # "pass" es palabra reservada para que la funcion este escrita y no te de error

print('-------------funcion--------------------')
def my_first_function():
  print('Hello World!')

my_first_function() #Es una forma de llamar a la funcion

print('--------------funcion dentro de funcion-------------------')
#podemos llamar funciones dentro de funciones

def my_second_function():
  my_first_function() 

my_second_function()

print('-------------funcion con parametros--------------------')
# paso de parametros dentro de las funciones

def say_hi(name):
  print('HI {}'.format(name))

say_hi("Diego")

print('-------------funcion con args--------------------')
# si no sabemos el numero de argumentos podems pasar un '*' delante del paramtro, por convención en python el parametro se llamra 'args'

def my_car_list(*args):
  print(args) #podemos ver todos los parametros pasados
  print(args[1]) #podemos tener uno de los parametros

my_car_list('nissan', 'chevrolet', 'honda')

print('------------funcion con argumentos ---------------------')
# podemos pasar los argumentos con nombre

def my_name_is(firstName, lastName):
  print(firstName, lastName)

my_name_is(lastName='Tinitana', firstName='Diego') # no importa el orden de los argumentos como esta nombrados los reconoce en su orden

print('------------funcion con kwargs---------------------')
# si no sabemos cuantos argumentos  pasar con nombre

def my_color(**kwargs):
  print(kwargs)
  print(kwargs['color1'])

my_color(color1='red',  calor2='blue')

print('------------funciones con una funcion de parametro---------------------')

def my_one_fuction():
  print('my function was executed')

def my_two_fuction(fucn):
  fucn()

my_two_fuction(my_one_fuction)

print('------------funciones recursivas-----------------')

def recursion(k):
  if(k > 0):
    result = k + recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
recursion(6)

print('------------funciones que retorne valor-----------------')

def say_hello(name):
  return 'say hello {}'.format(name.upper())

hello = say_hello('diego')
print(hello)

'''
Mas informacion:
https://www.w3schools.com/python/python_functions.asp
https://docs.python.org/3/
'''