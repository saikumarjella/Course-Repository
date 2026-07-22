##String##
##you can put strings in single quote, double quote or triple quote

x= 'single quote'
print(type(x))

x = "double quote, you can use 'single quote in here' "
print(type(x))

x = '''this is a triple quote, 
you can write in multiple lines like this also you can use "double quotes" in it as this'''
print(type(x))

##Strings can also be indexed

x = 'Good Morning!'
print(x[:4])
print(x[5])
print(x[-3])

print(x*3)
print(x+x)