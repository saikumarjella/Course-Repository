##Lists
#Lists can store multiple values

x = [1,2,3]
print(type(x))
print(x)

#Lists are also indexed as strings are indexed

x = ['red','blue','orange']
print(type(x))

#Lists can have any datatype within them 

x = [1,'red', ['blue','orange'],True]
print(type(x))

#Lists are also really good because we can add or delete items within it

x = ['red','blue','orange']
x.append('white')
print(x)
x[0] = 'black'
print(x)

#Nested List
x = [1,'red', ['blue','orange'],True]
print(x[0])
print(x[2])
print(x[2][1])