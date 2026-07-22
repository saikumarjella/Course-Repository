##Dictionaries
# Dictionaries have something called a Key/Value pair

x = {'name':'Saikumar', 'gender': 'Male', 'favorite games': ['Cricket','Kabaddi']}
print(type(x))
print(x)

print(x.values())
print(x.keys())
print(x.items())

#you cannot call a dictionary by an index you can call it by keys
#print(x[0])
print(x['name'])

#you can also change stuff in dictionaries
x['name'] = 'Sai'
print(x)

#you can also use functions like update which updates the whole dictionary
#this doesnt delete the already existing key value pairs
x.update({'name': 'Saikumar','gender':'Male', 'Hair Color':'Black'})
print(x)

#you can also delete stuff from dictionary using del keyword
del x['Hair Color']
print(x)