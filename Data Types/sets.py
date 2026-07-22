##They are somewhat similar to lists and tuples
##They dont have any duplicate elements and also sets are not indexed

x = {1,2,3}
print(type(x))
print(x)

#the duplicates are removed i.e, we only get unique values
y = {1,2,1,4,7,7,3,2}
print(y)

#we can compare sets
#This will show only the uniques values in both the sets
print(x|y)
#This will show that show up in both sets
print(x&y)
#This will show us what doesnt match
print(x-y)
print(y-x)
#This will show the completely unique values in either of these but will not show the common values
print(x^y)