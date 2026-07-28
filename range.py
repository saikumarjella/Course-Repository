# the syntax of range is
# range(start, stop, step-size)
# all the arguments needs to be integer and step size cannot be 0

a = range(0,5)
b = range(5)

print(a)
print(b)

print(a[0])
print(b[4])

a = range(2,5)
for i in a:
    print(i)

a = range(2,10,2)
for i in a:
    print(i)

a = range(2, 10, -1) #for range(i,j,k) the seq is i, i+k, i+2k, .....j-k
for i in a:
    print(i)

a = range(-1,-10,-1)
for i in a:
    print(i)