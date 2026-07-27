print(round(5),type(round(5)))
print(round(5,2),type(round(5,2)))
print(round(5.84),type(round(5.84)))
print(round(5.9876,2),type(round(5.9876,2)))
print(round(5.8667,0),type(round(5.8667,0)))
print(round(5.7),type(round(5.7)))

#round can have positve, zero or negative numbers in its second argument

print(round(589,2),type(round(589,2)))
print(round(589,0),type(round(589,0)))
print(round(589,-1),type(round(589,-1)))#for round(num,-n) returns closest multiple of 10**n to the num
print(round(589,-3),type(round(589,-3)))
print(round(589,-4),type(round(589,-4)))#will return 0 as no. of digits exceeds the number of digits of number 