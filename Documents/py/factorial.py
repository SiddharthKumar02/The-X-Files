import time

start = time.time()

f = int(input("Enter number: "))
fact = 1
cnt = f
while cnt > 0:
        fact = fact * cnt
        cnt = cnt - 1
print 'Factorial = ', fact

print 'Number of digits is ', (len(str(fact)))

stop = time.time()

print'Clock speed = ', (stop - start)
