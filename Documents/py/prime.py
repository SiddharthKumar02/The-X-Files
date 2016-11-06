n = int(input("Enter number: "))
found = 0
N = n
while N > 0:
    if(n % N == 0):
        found = found + 1
    N = N - 1
if found == 2:
    print("This is a prime")
else:
    print("This is not a prime")
