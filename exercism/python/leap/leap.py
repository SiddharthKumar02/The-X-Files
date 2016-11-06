count = int(input("Enter count: "))
while count > 0:
	l = int(input("Enter an year: "))
	if l % 4 == 0 and (l % 100 != 0 or l % 400 == 0):
		print("Leap year")
	else:
		print("Not a leap year")
	count -= 1
	if count == 0:
	 break

