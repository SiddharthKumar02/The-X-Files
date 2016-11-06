import time
print("This is the timer")
# Ask to Begin
start = input("Would you like to begin Timing? (y/n): ")
if start == "y":
    timeLoop = True
else:
    timeloop = False
    print("Still gonna show you the timer. XD")

# Variables to keep track and display
Sec = 0
Min = 0
# Begin Process
timeLoop = start
while timeLoop:
    Sec += 1
    print(str(Min) + " Mins " + str(Sec) + " Sec ")
    time.sleep(1)
    if Sec == 60:
        Sec = 0
        Min += 1
        print(str(Min) + " Minute")
