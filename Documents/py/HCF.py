a = raw_input("Enter a number: ")
b = raw_input("Enter another number: ")
a = int(a) 
b = int(b)

if a > b:
    x = a
else:
    x = b

for i in range(1, x):
    if a % i == 0 and b % i==0:
        HCF = i

print 'HCF of both is: ', HCF
	
	
	
