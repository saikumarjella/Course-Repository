colors = ['red','blue','green']

for color in colors:
    print(color)

name = 'Johndoe'

for letter in name:
    print(letter)

#break control statement

for letter in name:
    print(letter)
    if letter == 'n':
        break

for letter in name:
    if letter == 'n':
            break
    print(letter)
    
#continue control statement

for letter in name:
    print(letter)
    if letter == 'n':
         continue
    

#else in for loop
#else in a for loop specifies a block of code to be executed when the for loop iterates through all its variables succesfully

for num in range(5):
    print(num)
else:
    print('finished for loop succesfully!') #else will not be executed if we use break to stop a loop

for num in range(5):
    if num == 2:
        break
    print(num)
else:
    print('finished for loop succesfully!')

#nested for loop

color = ['red', 'black', 'white']
clothes = ['shirt', 'pant', 'jacket']

for c in color:
    for i in clothes:
        print(c,i)

#pass statement, for loops cannot be empty we use pass to skip that statement for now

for i in range(100):
    pass