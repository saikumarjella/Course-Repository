#lambda function is a anonymous function
# it can have any number of arguments but only a single expression

## lambda arguments : expression

x = lambda a: a + 5
print(x(5))

y = lambda a,b : a * b
print(y(5,6))

z = lambda a, b, c : a + b + c
print(z(1,2,3))

#lambda is best used inside an other function

def n_times(n):
    return lambda a : a*n

double = n_times(2)
print(f'the double of 586 is {double(586)}')

triple = n_times(3)
print(f'the triple of 586 is {triple(586)}')
#lambda is created when we need a function for short period of time

###lambda is mainly used with map(), filter() and sorted() functions.

#map(function, iterable)
marks = [45, 56, 98, 85, 76 , 92, 63]

def grade(marks):
    if marks >= 90:
        return 'O'
    elif 80 <= marks < 90:
        return 'A'
    elif 70 <= marks < 80:
        return 'B'
    elif 60 <= marks < 70:
        return 'C'
    else:
        return 'F'

grades = list(map(grade, marks))


#grades = list(map(grade, marks))

print(f'marks are {marks}')
print(f'grades are {grades}')   
#print(f'grades are {next(grades)}') 

#print(f'grades are {list(grades)}')

#filter filters variables from a datatype.

def fail_score(score):
    return score < 60

result = list(filter(fail_score, marks))
print(f'the failing scores are {result}')

result_lambda = list(filter(lambda a: a<60, marks))
print(f'the failing scores are {result_lambda}')