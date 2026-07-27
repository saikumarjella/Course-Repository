# if condition:
#     Statements to execute if condition is true
# else:
#     Statements to execute if condition is false

condition = True

# if condition:
#     print('inside if block')
# else:
#     print('inside else block')

# print('outside if else block')      

#Nested if else statement
if condition:
    print ('Statements to execute if condition is true')
    if condition:
        print ('Statements to execute if condition is true')
    else:
        print ('Statements to execute if condition is false')
else:
    print ('Statements to execute if condition is false')

# if condition:
#     print('inside main if block')
#     if not condition:
#         print('inside nested if block')
#     else:
#         print('inside nested else block')
# else:
#     print('inside main else block')

# num = int(input('enter a number:'))

# if num%2 == 0:
#     print(f'{num} is a even number')
#     if num%5 == 0:
#         print(f'{num} is also divisible by 5')
#     else:
#         print(f'{num} is not divisible by 5')
# else:
#     print(f'{num} is an odd number')