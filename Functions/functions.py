#a function can be defined like this:
def my_function():
    print('Hello from a function')

#a function will be called like this, you can also call a function multiple times
my_function()
my_function()
my_function()

#converting kmph to mps

def kilo_to_meter(kilometer):
    meter = kilometer*(5/18)
    return round(meter,2)

#without functions you have write the same code multiple times
kilo1 = 55
meter1 = round(kilo1*(5/18),2)
print(f'{meter1} m/s')

kilo2 = 100
meter2 =round(kilo2*(5/18),2)
print(f'{meter2} m/s')

kilo3 = 150
meter3 = round(kilo3*(5/18),2)
print(f'{meter3} m/s')

#with function you can write once and reuse the code

print(f'{kilo_to_meter(kilo1)} m/s')
print(f'{kilo_to_meter(kilo2)} m/s')
print(f'{kilo_to_meter(kilo3)} m/s')
#here the function returned a value which we directly used in a print function, we could
#also store this returned value in an other variable and use it instead
#### If a function doesnt have a return statement, it returns None by default####

#we can also use pass statement in functions as a function placeholder

def use_later():
    pass