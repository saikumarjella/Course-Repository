#a function with arguments
def my_name(name):#name is the parameter
    print(f'my name is {name}')

my_name('Saikumar') #'Johndoe' is the argument

#function should be called with the number of arguments it expects

def full_name(fname, lname):
    print(f'my full name is {fname} {lname}')

full_name('Sai', 'kumar')
#full_name('Johndoe')

####Default Parameter values######

def my_func(color = 'white'):
    print(f'The color of my shirt is {color}')

my_func('red')
my_func('blue')
my_func()

###Key word arguments also can be called as kwargs####
def key_word(name, color):
    print(f'Hi, my name is {name} and my favorite color is {color}')

key_word(color = 'red', name = 'Saikumar')
key_word('Sai', 'White')#positional arguments, order matters here
key_word('Saikumar', color = 'blue') #you can also mix kwargs and positional arguments

##different datatypes in functions###

def list_func(colors):
    for color in colors:
        print(color)

def dict_func(details):
    print(details.items())
    print(f'hi, my name is {details['name']}, my age is {details['age']} and I am a {details['occupation']}.')

my_colors = ['red','white','blue']
list_func(my_colors)

my_details = {'name': 'Saikumar', 'age': 25, 'occupation': 'doctor'}
dict_func(my_details)


#### return in Functions ########
#these retuen values can be of any data type

def add(x,y):
    return x+y

print(add(5,6))

def string():
    return ['red','white']

colors = string()
for color in colors:
    print(color)

def tup():
    return (5,6)
x,y = tup()
print(f'x is {x} and y is {y}')

#####Position only arguments###

def pos(name,/):
    print(f'my name is {name}')

pos('Saikumar')
#pos(name = 'Saikumar')

##### Key word only arguments#####

def key(*,name):
    print(f'my name is {name}')

#key('Saikumar')
key(name = 'Saikumar')

####combining positional and keyword only arguments#######

def both(x,y,/,*,a,b):
    return x+y+a+b

sum = both(5, 6, b = 8,   a = 7)
print(sum)