#while loop can execute a set of statements as long as condition is true

# while condition:
#     statements

num = 1
while num < 5:
    print(num) 
    num += 1 # you have to increment num here if not loop will run indefinitely

#while needs to have a relevent variable to be ready and be incremented.

#break in while

num = 1
while num < 5:
    print(num)
    if num == 3:
        break
    num += 1

#continue in while
num = 1
while num < 5:
    num += 1
    if num == 3:
        continue
    print(num)

#else in while
#the control goes to else block when condition is no longer true

num = 1
while num < 5:
    print(num)
    num += 1
else:
    print('num is not less than 5')

num = 1
while num < 5:
    print(num)
    if num == 3:
        break
    num += 1
else:
    print('num is not less than 5')

num = int(input('enter a number(enter -1 to stop)'))# -1 is called sentinel value here

while num != 7: 
    print(num); 
    num = int(input('enter a number(enter -1 to stop)'))