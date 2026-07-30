x = 100 #Global Scope

def my_func():
    x = 50 #Local Scope
    print(f'value of x in the function is {x}')

my_func()
print(f'value of x in the main body is {x}')

#If a local and global variable have the same name inside and outside functions
#python will treat them as different variables, one in local the other in global

#If you want to create a global variable in a function or in a local scope you can use the keyword global

def global_var():
    global a
    a = 25

global_var()
print(f'the value of a is {a}')

#we can also use global keyword to change the values of a global variable in a function

b = 200

def change_global():
    global b
    b = 100

change_global()
print(f'the value of b is {b}')

# if we use nonlocal keyword, the variable will belong to the outer function

def nonlocal_var_outer():
    x = 'Hello'
    def nonlocal_var_inner():
        #nonlocal x
        x = 'World'
    nonlocal_var_inner()
    return x
print(f'the value of x is {nonlocal_var_outer()}')

####LEGB RULE########

g = 'global'

def outer_func():
    g = 'enclosing'
    def inner_func():
        g = 'local'
        print(f'inner function variable is: {g}')
    inner_func()
    print(f'outer function variable is {g}')

outer_func()
print(f'vaiable inside main code is: {g}')