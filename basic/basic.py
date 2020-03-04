# Comentario en python se pueden hacer con el # o tambiem entre ''' ''' """ """
# Este es un comentario de una sola linea 
""" Este es un comentario
de varias Lineas"""

'''Las comillas simples
son igual q las comillas dobles'''

# declarar variables 
print('---------------------------------')
my_name = 'Diego'
my_var = 12
print(my_name, my_var)
# tipos de variables
print('----------------variables-----------------')
'''
Text Type:	str
Numeric Types:	int, float, complex: son numeros imaginarion se los escribe con una j al final
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
'''
#ejemplos de variables 
my_str = "hello world" #constructor str()
my_int = 1 #constructor int()
my_float = 2.05 #constructor float()
my_complex = 1j 
my_list = ["a","b",[1,2], "c"] #son arrays mutables se los representa [ ] constructor list()
my_tuple = ("a", "b", {"a": "1"}) #son arrays inmutables se los representa ( ) constructor tuple()
my_ranger = range(4) # retorna un rango (0, 4) y puede ser recorrido
my_dict = {"a": "1", "b":"2", "c":{"z": 30}} #constructor dict()
my_set = set(("apple", "banana", "cherry")) # no permite datos repetidos y es mutable constructor set()
my_frozenset = frozenset(("apple", "banana", "cherry")) # no permite datos repetidos y es inmutable
my_bool = True or False

print("more vars: " + my_str)
print("vars: {}, {}, {}, {}, {}, {}".format(my_int, my_float, my_complex, my_list, my_tuple, my_ranger))
print('------------variables type---------------------')
#podemos saber que tipo de variable es con el metodo type()

print("types: ", type(my_str), type(my_int), type(my_bool))
print('--------------casting-------------------')
# transformar variables con los metodos int(), float(), str()

x = "12"
print("x es de typo str: ",type(x))
x_int = int(x)
print("x_int es entero:", type(x_int))
my_number = "3"
print("my_number {} es un string:".format(my_number), type(my_number))
print("my_number {} ahora es un int: ".format(int(my_number)), type(int(my_number)))
print("my_number {} ahora es float: ".format(float(my_number)), type(float(my_number)))

# si queremos transformar un str: "diego" a float o int tendremos este error 'could not convert string to float: 'diego''

print('-------------operators--------------------')

#operadores aritmeticos:

my_addition = 1 + 2 #return: 3
my_subtraction = 2 - 1 #return: 1
my_muilt = 2 * 2 #return: 4
my_division = 5 / 2 #return: 2.5
my_modulus = 37 % 3 #return: 1
my_exponentation = 3 ** 3 #return: 27
my_floor_division = 5 // 2 #return: 2

#operadores de asignacion: 

x = 5 #  same as x = 5
x += 3 # same as x = x + 3
x -= 3 # same as x = x - 3
x *= 3 # same as x = x * 3
x /= 3 # same as x = x / 3
x %= 3 # same as x = x % 3
x //= 3 # same as x = x // 3
x **= 3 # same as x = x ** 3

#operadores de Comparación
x = 0
y = 1

x == y # Igual
x != y # No es igual
x > y # es mayor que 
x < y # es menor que 
x >= y # es mayor o igual  que 
x <= y # es menor o igual que 

#operadores logicos

x < 5 and x < 10 # same as && 
x > 5 or x < 10 # same as || 
not(x< 5 and x < 10) # same as !=

#operadores de identidad: no revisa q sean el mismo objeto si el objeto esta en el mismo espacio de memoria 

x is y # retorna verdadero si la variable es el mismo objeto
x is not y # retorna verdadero si la variable no es el mismo objeto 

# if else elif
print('-------------if elif else--------------------')
if x > y:
  print(x)
elif y == x:
  print(y)
else:
  print('x < y', '\n')
print('--------------list-------------------')
# Metodos mas usados de las listas igual para tuplas,  dict y strings

my_list = [1, 2, 3, 4, 5]
print(my_list[0]) # obtiene el segundo valor de la lista [1]
print(my_list[-1]) # obtiene el ultimno valor de la lista [5]
print(my_list[0:3]) # obtenemos un rango de la lista [1, 2, 3]
print(my_list[:2])  # obtenemos un rango de la lista desde el inicio hasta el rango [1, 2]
print(my_list[2:])  # obtenemos un rango de la lista desde el indice hasta el final [3, 4, 5 ]
print(my_list[-3:-1]) # obtenemos un rango de numeros contando desde atras [3, 4]
print('---------------------------------')

my_list[0] = 20 # es la forma de cambiar el valor de un elemento dentro de la lista esto no funciona con las tuplas proque son inmutables
my_str_name = "Diego"
print(my_str_name[0], '\n')

print('-------------loop list--------------------')
#recorridos en las listas, tuplas, dict y string
for x in my_list:
  print(x)
print('--------------loop string-------------------')
for letter in my_str_name:
  print(letter)
print('-------------search in list--------------------')
#revisar si existe un elemento en las listas, tuplas, dict y string

if 2 in my_list:
  print('si existe el 2')

if 'D' in my_str_name:
   print('si existe', 'd')
print('-------------tamaño de la lista  list--------------------')
# podemos sacar la longitud con metodo len()
print(len(my_list))

print('-------------add item in list--------------------')
# add  un elemento en las listas, dict y string con los metodos insert() append()

my_list.append(6)
my_list.insert(1, 1) #necesita el index donde se quiere ponder el elemento y el elemento q se va añadir 
print(my_list)
print('-------------remove item in list--------------------')

# Remover un elemento en las listas, dict y string con los metodos remove() pop()
my_list.remove(6) # elimina un item especifico
my_list.pop(0) # elimina el ultimo elemento si no se especifica el index
print(my_list)
print('------------clean list---------------------')

# Remover un elemento en las listas, dict y string con los metodos del() clear()
remove_list = ['a', 'b', 'c', 'd']
print(remove_list)
del remove_list[1] # elimina un item especifico con el index y si no se declara el index se elimina toda la lista
print(remove_list)
remove_list.clear() # elimina la lista
print(remove_list)
print('-------------copy list--------------------')

# Copiar Listas, typlas, dict con el metodo copy() o list()
list_a = [1, 2, 3, 4, 5, 6]
list_b = list_a # esto es copia por referencia si se cambia la lista b tambien se vera afectada la lista a

copy_list = list_a.copy() #esto hace una copia real de la lista a hacia copy list
copy_list_two = list(copy_list)
copy_list.append(7)
print('lista_a: ', list_a)
print('copy_list: ', copy_list)
print('copy_list_two: ', copy_list_two)

print('-------------Join lists--------------------')
# Copiar Listas, dict con el metodo append() o extend()
join_list = copy_list + copy_list_two
print('join_list: ', join_list)

for x in copy_list_two:
  copy_list.append(x)
print('copy_list: ', copy_list)

copy_list.extend(copy_list_two)
print('copy_list: ', copy_list)

print('-------------for loop--------------------')

fruits = ["apple", "banana", "cherry"]
for x in fruits: # recorremos una lista 
  print(x)
print('\n')
fruits = ("apple", "banana", "cherry")
for x in fruits: # recorremos una tupla 
  print(x)
print('\n')
for x in 'banana': #recorremos un array
  print(x)
print('\n')
for x in range(6): # recorremos un range
  print(x)

print('-------------for anidados--------------------')
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj: #primer for
  for y in fruits: # segundo for
    print(x, y)

print('-------------for con else--------------------')
for x in range(6):
  print(x)
else:
  print("Finally finished!")

print('-------------diccionarios--------------------')

my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(my_dict)
print('el valor es:', my_dict['brand']) # podemos recuperar el valos mediante la llave
print('el valor es:', my_dict.get('model')) # podemos recuperar el valos mediante la llave mediate el metodo get()
# podemos cambiar el valor mediante la llave
my_dict["year"] = 2020
print(my_dict)
print('\nloops con llaves')
for x in my_dict:
  print(x)
print('\nloops con valor')
for x in my_dict.values():
  print(x)

print('\nloops con llave y valor')
for x, y in my_dict.items():
  print(x, y)

print('\nsaber si una llave existe')
if "model" in my_dict:
  print('si existe')

#copiar un diccionario es igual q las listas con el metodo copy() o dict()
#para eliminar un item del diccionario tambien tenemos otro metodo popitem()
print(my_dict.popitem()) # elimina el ultimo item si no se especifica la llave


'''
Para mas informacion pueden reviar los siguientes 
links de donde se saco la informacion.
https://www.w3schools.com/python/default.asp
https://www.youtube.com/watch?v=y-ZzTGHFEhI&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM&index=42
https://docs.python.org/3/.

Tambien hay información sobre buenas practicas de desarrollo en python.
https://www.python.org/dev/peps/pep-0008/

Para ejecutar todos los ejercicios de esta sección abra la consola vaya a la carpeta donde
se encuentra el archivo y ejecute "python3 basic.py"
'''