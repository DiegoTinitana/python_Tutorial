'''
Un decorador es un funcion que crea funciones y ejecuta funciones
'''

print('-------------decoradores--------------------')
def decorator(func):
  def new_function():
    print('vamos ejecutar la funcion')
    func()
    print('ejecutamos la funcion')
  return new_function

@decorator
def say_hello():
  print('say hello')

say_hello()


print('-------------decoradores con funciones y parametros --------------------')

def first_decorator(func):
  def new_function(*args, **kvargs):
    print('vamos ejecutar la funcion')
    result = func(*args, **kvargs)
    print('ejecutamos la funcion')
    return result
  return new_function

@first_decorator
def sum(a, b):
  return a + b
result = sum(2, 4)
print(result)


print('-------------decoradores con parametros --------------------')

def second_decorator(is_valid = True):
  def _second_decorator(func):
    def before_action():
      print('vamos ejecutar la funcion')
    
    def after_action():
      print('ejecutamos la funcion')

    def new_function(*args, **kvargs):
      if is_valid:
        before_action()
      result = func(*args, **kvargs)
      after_action()
      return result
    return new_function
  return _second_decorator

@second_decorator(is_valid = False)
def muilt(a, b):
  return a * b
result = muilt(2, 4)
print(result)

'''
Mas informacion:
https://www.geeksforgeeks.org/decorators-in-python/
https://docs.python.org/3/
'''