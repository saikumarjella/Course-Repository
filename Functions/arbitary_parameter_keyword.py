def my_func(*colors):
    print(type(colors)) #arbitary arguments are always passed as tuples
    print(f'the first color is {colors[0]}')
    print(f'the second color is {colors[1]}')
    print(f'the third color is {colors[2]}')
    print(f'all the colors are {colors}')

my_func('red','blue','white')

#you can combine both regualr and arbitary parameters(*args), regular parameters must come first

def total(sum,*numbers):
    for num in numbers:
        sum += num
    return sum

print(total(0, 1, 2, 3, 4, 5))
print(total(0,10,20,30))
print(total(5))

def max(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(max(1,15,4,25,6,7))

#### arbitary keywords Argumets **kwargs ############

def my_details(**details):
    print(type(details))
    print(f'all my details are: {details}')
    print(f'my full name is {details['fname']} {details['lname']}, my age is {details['age']} and my occupation is {details['occupation']}')

my_details(fname = 'Sai', lname = 'kumar', age = 23, occupation = 'Job')

### you can combine regular parameters with **kwargs

def user_details(username, **userdetails):
    print(f'username: {username}')
    for key, value in userdetails.items():
        print(f'additional details {key} : {value}')

user_details('Saikumar', age = 23, occupation = 'Job')

### you can also combine *args and **kwargs ####
#### the order must be regular parameters followed by *args followed by **kwargs ####

def func(title, *args, **kwargs):
    print(f'Title : {title}')
    print(f'Positional arguments : {args}')
    print(f'Keyword arguments : {kwargs}')

func('user info', 'saikumar','saikumar', age = 23, city = 'New york')

##you can unpack lists and dictionaries using * and ** respectively when calling functions into individual arguments

def example(a,b,c):
    return a+b+c

numbers = [1,2,3]
result = example(*numbers) # same as: example(1,2,3)
print(result)

def example_2(fname,lname):
    print(f'Hello {fname} {lname}')

person = {'fname':'Sai', 'lname':'kumar'}
example_2(**person) #same as: example_2(fname = 'Sai', lname = 'kumar')